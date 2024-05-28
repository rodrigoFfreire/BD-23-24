from datetime import datetime
from .exceptions import InvalidInput, NonExistentValue

DATE_FORMAT = "%Y-%m-%d"
TIME_FORMAT = "%H:%M"

def is_valid_datetime(datetime_str: str, format_str: str):
    try:
        datetime.strptime(datetime_str, format_str)
        return True
    except ValueError:
        return False
    
def is_time_later(date_str, time_str):
    # Date and time are assumed to be in the valid format
    now = datetime.now()
    
    date = datetime.strptime(date_str, DATE_FORMAT)
    time = datetime.strptime(time_str, TIME_FORMAT)
    
    if date > now.date() or (date == now.date and time > now.time()):
        return True
    return False
    
def parse_appointment_input(pacient, doctor, date, time):
    if pacient is None or doctor is None or date is None or time is None:
        raise InvalidInput("Missing fields")
    if not is_valid_datetime(date, DATE_FORMAT):
        raise InvalidInput("Invalid date format")
    if not is_valid_datetime(time, TIME_FORMAT):
        raise InvalidInput("Invalid time format")
    if not is_time_later(date, time):
        raise InvalidInput("date and time supplied are in the past")