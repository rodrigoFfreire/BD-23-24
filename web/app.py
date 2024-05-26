#!/usr/bin/python3

import os
import datetime
from logging.config import dictConfig

import psycopg
from flask import Flask, jsonify, request
from psycopg.rows import namedtuple_row

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
DB_URL = os.environ.get("DATABASE_URL", "postgres://app:app@postgres/deez")


def is_valid_date(date_str):
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def is_valid_time(time_str):
    try:
        datetime.datetime.strptime(time_str, "%H:%M")
        return True
    except ValueError:
        return False


# ROUTES
@app.route("/", methods=("GET",))
def list_all_clinics():
    # TODO
    log.debug("Listing all clinics...")
    return jsonify({"message": "Clinics: ..."}), 501  # Change this to 200 (OK) when implemented


@app.route("/c/<clinica>/registar", methods=("POST",))
def schedule_appointment(clinica):
    # TODO
    pacient = request.args.get("pacient")
    doctor = request.args.get("doctor")
    date = request.args.get("date")
    time = request.args.get("time")

    if pacient is None or doctor is None or date is None or time is None:
        return jsonify({"error": "Missing fields"}), 400
    if not is_valid_date(date):
        return jsonify({"error": "Incorrect date format"}), 400
    if not is_valid_time(time):
        return jsonify({"error": "Incorrect time format"}), 400

    log.debug(f"Scheduling appointment at clinic \'{clinica}\'. Received args: {pacient}, {doctor}, {date}, {time}")
    return jsonify({
        "pacient": pacient,
        "doctor": doctor,
        "date": date,
        "time": time
    }), 501  # Change this to 204 (No Content) when implemented and return ""


@app.route("/c/<clinica>/cancelar", methods=("POST",))
def cancel_appointment(clinica):
    # TODO
    pacient = request.args.get("pacient")
    doctor = request.args.get("doctor")
    date = request.args.get("date")
    time = request.args.get("time")

    if pacient is None or doctor is None or date is None or time is None:
        return jsonify({"error": "Missing fields"}), 400
    if not is_valid_date(date):
        return jsonify({"error": "Incorrect date format"}), 400
    if not is_valid_time(time):
        return jsonify({"error": "Incorrect time format"}), 400

    log.debug(f"Canceling appointment at clinic \'{clinica}\'. Received args: {pacient}, {doctor}, {date}, {time}")
    return jsonify({
        "pacient": pacient,
        "doctor": doctor,
        "date": date,
        "time": time
    }), 501  # Change this to 204 (No Content) when implemented and return ""


@app.route("/c/<clinica>", methods=("GET",))
def list_clinic_specialties(clinica):
    # TODO
    log.debug(f"Listing specialties of clinic \'{clinica}\'")
    return jsonify({"message": f"Specialties of clinic \'{clinica}\': ..."}), 501  # Change this to 200 (OK) when implemented


@app.route("/c/<clinica>/<especialidade>", methods=("GET",))
def list_specialty_doctors(clinica, especialidade):
    # TODO
    log.debug(f"Listing \'{especialidade}\' doctors from clinic \'{clinica}\'")
    return jsonify({"message": f"\'{especialidade}\' doctors from clinic \'{clinica}\': ..."}), 501  # Change this to 200 (OK) when implemented


# Just for debugging purposes. Remove this later
@app.route("/ping", methods=("GET",))
def ping():
    try:
        with psycopg.connect(conninfo=DB_URL) as conn:
            with conn.cursor(row_factory=namedtuple_row) as cur:
                test_data = cur.execute(
                    """
                    SELECT *
                    FROM test_table
                    """
                ).fetchall()
                log.debug(f"Found {cur.rowcount} rows.")
        return jsonify(test_data)
    except psycopg.Error as err:
        log.debug(err)
        return jsonify({"error": "Could not execute query"}), 500


if __name__ == "__main__":
    app.run()
