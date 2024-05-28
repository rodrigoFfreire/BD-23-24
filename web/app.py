#!/usr/bin/python3
import os
import sys
sys.path.append('/app/web')

from logging.config import dictConfig

import psycopg
from flask import Flask, jsonify, request
from psycopg.rows import namedtuple_row

from utils.validators import *
from queries.queries import *

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s:%(lineno)s - %(funcName)20s(): %(message)s",
            }
        },
        "handlers": {
            "wsgi": {
                "class": "logging.StreamHandler",
                "stream": "ext://flask.logging.wsgi_errors_stream",
                "formatter": "default",
            }
        },
        "root": {"level": "INFO", "handlers": ["wsgi"]},
    }
)

app = Flask(__name__)
app.config.from_prefixed_env()
log = app.logger
DB_URL = os.environ.get("DATABASE_URL", "postgres://app:app@postgres/app")


# ROUTES
@app.route("/c/<clinica>/registar", methods=("POST",))
def schedule_appointment(clinica):
    pacient = request.args.get("pacient")
    doctor = request.args.get("doctor")
    date = request.args.get("date")
    time = request.args.get("time")

    try:
        parse_appointment_input(pacient, doctor, date, time)
    except InvalidInput as e:
        log.debug(e)
        return jsonify({"error": e}), 400

    # TODO


@app.route("/c/<clinica>/cancelar", methods=("POST",))
def cancel_appointment(clinica):
    pacient = request.args.get("pacient")
    doctor = request.args.get("doctor")
    date = request.args.get("date")
    time = request.args.get("time")
    
    try:
        parse_appointment_input(pacient, doctor, date, time)
    except InvalidInput as e:
        log.debug(e)
        return jsonify({"error": e}), 400

    # TODO


@app.route("/", methods=("GET",))
def list_all_clinics():
    try:
        with psycopg.connect(conninfo=DB_URL) as conn:
            conn.read_only = True
            with conn.cursor(row_factory=namedtuple_row) as cur:
                data = cur.execute(LIST_CLINICS_QUERY).fetchall()
                log.debug(f"Fetched {cur.rowcount} clinics.")
        return jsonify(data)
    except psycopg.Error as e:
        log.debug(e)
        return jsonify({"error": "Could not complete this request"}), 500


@app.route("/c/<clinica>", methods=("GET",))
def list_clinic_specialties(clinica):
    try:
        with psycopg.connect(conninfo=DB_URL) as conn:
            conn.read_only = True
            with conn.cursor(row_factory=namedtuple_row) as cur:
                clinic_name = cur.execute(FIND_CLINIC_QUERY, {"clinic_name": clinica})
                check_clinic_name(clinic_name)
            
                data = cur.execute(LIST_SPECIALTIES_QUERY, {"clinic_name": clinica}).fetchall()
                log.debug(f"Fetched {cur.rowcount} specialties from clinic {clinica}")
        return jsonify(data)
    except NonExistentValue as e:
        log.debug(e)
        return jsonify({"error": e}), 400
    except psycopg.Error as e:
        log.debug(e)
        return jsonify({"error": "Could not complete this request"}), 500
    

@app.route("/c/<clinica>/<especialidade>", methods=("GET",))
def list_specialty_doctors(clinica, especialidade):
    try:
        data = []
        with psycopg.connect(conninfo=DB_URL) as conn:
            conn.read_only = True
            with conn.cursor(row_factory=namedtuple_row) as cur:
                clinic_name = cur.execute(FIND_CLINIC_QUERY, {"clinic_name": clinica})
                check_clinic_name(clinic_name)
                
                doctor_names = cur.execute(
                    LIST_SPECIALTY_DOCTORS_QUERY, 
                    {"clinic_name": clinica, "specialty": especialidade},
                ).fetchall()
                log.debug(f"Fetched {cur.rowcount} doctors from clinic {clinica} specialized in {especialidade}.")
                
                for name in doctor_names:
                    schedules = cur.execute(
                        LIST_DOCTOR_SCHEDULES_QUERY,
                        {"doctor_name": name[0]}
                    ).fetchmany(3)
                    
                    log.debug(f"Fetched {cur.rowcount} available schedules for doctor {name[0]}")
                    formatted_schedules = [
                        {'data': row.data.strfttime('%Y-%m-%d'), 'hora': row.hora.strftime('%H:%M')} 
                        for row in schedules
                    ]
                    data.append({"doctor": name[0], "schedules": formatted_schedules})
        return jsonify(data)
    except NonExistentValue as e:
        log.debug(e)
        return jsonify({"error": e}), 400
    except psycopg.Error as e:
        log.debug(e)
        return jsonify({"error": "Could not complete this request"}), 500


# Just for debugging purposes. Remove this later
@app.route("/ping", methods=("GET",))
def ping():
    try:
        with psycopg.connect(conninfo=DB_URL) as conn:
            with conn.cursor(row_factory=namedtuple_row) as cur:
                test_data = cur.execute(
                    """
                    SELECT nome
                    FROM test_table
                    """
                ).fetchall()
                log.debug(f"Found {cur.rowcount} rows.")
        print(test_data)
        return jsonify(test_data)
    except psycopg.Error as err:
        log.debug(err)
        return jsonify({"error": "Could not execute query"}), 500


if __name__ == "__main__":
    app.run()
