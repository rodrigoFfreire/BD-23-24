from datetime import datetime
from .exceptions import InvalidInput

import re

DATE_FORMAT = "%Y-%m-%d"
TIME_FORMAT = "%H:%M"
NIF_PATTERN = r'^\d{9}$'
SSN_PATTERN = r'^\d{11}$'

def is_valid_datetime(datetime_str: str, format_str: str):
    try:
        datetime.strptime(datetime_str, format_str)
        return True
    except ValueError:
        return False
    
def is_time_later(date_str, time_str):
    # Date and time are assumed to be in the valid format
    now = datetime.now()
    
    date = datetime.strptime(date_str, DATE_FORMAT).date()
    time = datetime.strptime(time_str, TIME_FORMAT).time()
    
    if date > now.date() or (date == now.date and time > now.time()):
        return date.isoweekday()
    return False
    
def parse_appointment_input(pacient_ssn, doctor_nif, date, time):
    if pacient_ssn is None:
        raise InvalidInput("Missing pacient SSN field")
    if doctor_nif is None:
        raise InvalidInput("Missing doctor NIF field")
    if date is None:
        raise InvalidInput("Missing appointment date field")
    if time is None:
        raise InvalidInput("Missing appointment time field")
    
    if re.match(SSN_PATTERN, pacient_ssn) is None:
        raise InvalidInput("Invalid pacient SSN")
    if re.match(NIF_PATTERN, doctor_nif) is None:
        raise InvalidInput("Invalid doctor NIF")
    
    if not is_valid_datetime(date, DATE_FORMAT):
        raise InvalidInput("Invalid date format")
    if not is_valid_datetime(time, TIME_FORMAT):
        raise InvalidInput("Invalid time format")
    if not is_time_later(date, time):
        raise InvalidInput("date and time supplied are in the past")