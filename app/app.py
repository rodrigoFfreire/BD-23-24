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
DB_URL = os.environ.get("DATABASE_URL", "postgres://saude:saude@postgres/saude")


# ROUTES
@app.route("/c/<clinica>/registar", methods=("POST",))
def schedule_appointment(clinica):
    pacient_ssn = request.args.get("pacient")
    doctor_nif = request.args.get("doctor")
    date = request.args.get("date")
    time = request.args.get("time")

    try:
        parse_appointment_input(pacient_ssn, doctor_nif, date, time)
    except InvalidInput as e:
        log.debug(e)
        return jsonify({"error": str(e)}), 400

    try:
        with psycopg.connect(conninfo=DB_URL) as conn:
            with conn.cursor(row_factory=namedtuple_row) as cur:
                cur.execute(
                    SCHEDULE_APPOINTMENT,
                    {"clinic_name": clinica, "pacient_ssn": pacient_ssn, "doctor_nif": doctor_nif,
                     "date": date, "time": time}
                )
        return jsonify({"message": "Appointment was scheduled successfully!"})
    except psycopg.IntegrityError as e:
        return jsonify(
            {"error": "Appointments can only be scheduled from 8h-13h and 14h-19h \
either on the hour or half hour."}), 400
    except psycopg.errors.RaiseException as e:
        return jsonify({"error": str(e).split('\n')[0]}), 400
    except psycopg.Error as e:
        log.debug(e)
        return jsonify({"error": "An unexpected error occured. Could not complete the request."}), 500


@app.route("/c/<clinica>/cancelar", methods=("POST",))
def cancel_appointment(clinica):
    pacient_ssn = request.args.get("pacient")
    doctor_nif = request.args.get("doctor")
    date = request.args.get("date")
    time = request.args.get("time")
    
    try:
        parse_appointment_input(pacient_ssn, doctor_nif, date, time)
    except InvalidInput as e:
        log.debug(e)
        return jsonify({"error": str(e)}), 400
    
    try:
        with psycopg.connect(conninfo=DB_URL) as conn:
            with conn.cursor(row_factory=namedtuple_row) as cur:
                cur.execute(
                    DELETE_APPOINTMENT,
                    {"clinic_name": clinica, "pacient_ssn": pacient_ssn, "doctor_nif": doctor_nif,
                     "date": date, "time": time}
                )
        return jsonify({"message": "Appointment was cancelled successfully!"})
    except psycopg.errors.RaiseException as e:
        return jsonify({"error": str(e).split('\n')[0]}), 400
    except psycopg.Error as e:
        log.debug(e)
        return jsonify({"error": "An unexpected error occured. Could not complete the request."}), 500


@app.route("/", methods=("GET",))
def list_all_clinics():
    try:
        with psycopg.connect(conninfo=DB_URL) as conn:
            conn.read_only = True
            with conn.cursor(row_factory=namedtuple_row) as cur:
                results = cur.execute(LIST_CLINICS).fetchall()
                log.debug(f"Fetched {cur.rowcount} clinics.")
        
        formatted_data = {"clinics": [{"clinic_name": clinic[0], "address": clinic[1]} for clinic in results]}
        return jsonify(formatted_data)
    except psycopg.Error as e:
        log.debug(e)
        return jsonify({"error": "An unexpected error occured. Could not complete the request."}), 500


@app.route("/c/<clinica>", methods=("GET",))
def list_clinic_specialties(clinica):
    try:
        print(len(clinica))
        with psycopg.connect(conninfo=DB_URL) as conn:
            conn.read_only = True
            with conn.cursor(row_factory=namedtuple_row) as cur:
                cur.execute(CHECK_CLINIC, {"clinic_name": clinica}) # Checks if clinic exists
            
                results = cur.execute(LIST_SPECIALTIES, {"clinic_name": clinica}).fetchall()
                log.debug(f"Fetched {cur.rowcount} specialties from clinic {clinica}")
                
        formatted_data = {"specialties": [specialty[0] for specialty in results]}
        return jsonify(formatted_data)
    except psycopg.errors.RaiseException as e:
        log.debug(e)
        return jsonify({"error": str(e).split('\n')[0]}), 400
    except Exception as e:
        log.debug(e)
        return jsonify({"error": "An unexpected error occured. Could not complete the request."}), 500
    

@app.route("/c/<clinica>/<especialidade>", methods=("GET",))
def list_specialty_doctors(clinica, especialidade):
    try:
        results = {"available_appointments": []}
        with psycopg.connect(conninfo=DB_URL) as conn:
            conn.read_only = True
            with conn.cursor(row_factory=namedtuple_row) as cur:
                cur.execute(CHECK_CLINIC, {"clinic_name": clinica}) # Checks if clinic exists
                
                doctors = cur.execute(
                    LIST_SPECIALTY_DOCTORS, 
                    {"clinic_name": clinica, "specialty": especialidade},
                ).fetchall()

                if not doctors:
                    return jsonify({"error": "The specified specialty doesnt exist."}), 400;

                log.debug(f"Fetched {cur.rowcount} doctors from clinic {clinica} specialized in {especialidade}.")
                for d in doctors:
                    schedules = cur.execute(
                        LIST_DOCTOR_SCHEDULES,
                        {"doctor_nif": d[1], "clinic_name": clinica}
                    ).fetchmany(3)
                    
                    log.debug(f"Fetched {cur.rowcount} available schedules for doctor {d[0]}")
                    formatted_schedules = [
                        {'data': row.data.strftime('%Y-%m-%d'), 'hora': row.hora.strftime('%H:%M')} 
                        for row in schedules
                    ]
                    results["available_appointments"].append({"doctor": d[0], "schedules": formatted_schedules})
        return jsonify(results)
    except psycopg.errors.RaiseException as e:
        return jsonify({"error": str(e).split('\n')[0]}), 400
    except Exception as e:
        log.debug(e)
        return jsonify({"error": "An unexpected error occured. Could not complete the request."}), 500


if __name__ == "__main__":
    app.run()
