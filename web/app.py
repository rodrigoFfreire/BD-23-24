#!/usr/bin/python3
import os
from logging.config import dictConfig

from flask import Flask, jsonify, request

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


###### ROUTES #####
@app.route("/", methods=("GET",))
def list_all_clinics():
    # TODO
    log.debug("Listing all clinics...")
    return jsonify({"message": "Clinics: ..."}), 501  # Change this to 200 (OK) when implemented


@app.route("/c/<clinica>/registar", methods=("POST",))
def schedule_appointment(clinica):
    # TODO
    data = request.get_json()
    print(data)

    pacient = data.get("pacient")
    doctor = data.get("doctor")
    date = data.get("date")
    time = data.get("time")

    if pacient is None or doctor is None or date is None or time is None:
        return jsonify({"message": "Bad Request"}), 400

    log.debug(f"Scheduling appointment at clinic \'{clinica}\'. Payload: {data}")
    return data, 501  # Change this to 200 (OK) when implemented


@app.route("/c/<clinica>/cancelar", methods=("POST",))
def cancel_appointment(clinica):
    # TODO
    data = request.get_json()

    pacient = data["pacient"]
    doctor = data["doctor"]
    date = data.get("date")
    time = data.get("time")

    if pacient is None or doctor is None or date is None or time is None:
        return jsonify({"message": "Bad Request"}), 400

    log.debug(f"Cancelling appointment at clinic \'{clinica}\'. Payload: {data}")
    return data, 501  # Change this to 200 (OK) when implemented


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


@app.route("/ping", methods=("GET",))
def ping():
    log.debug("ping!")
    return jsonify({"message": "pong!"}), 200


if __name__ == "__main__":
    app.run()
