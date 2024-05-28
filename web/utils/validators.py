from datetime import datetime
from exceptions import InvalidInput, NonExistentValue

def is_valid_datetime(datetime_str: str, format_str: str):
    try:
        datetime.strptime(datetime_str, format_str)
        return True
    except ValueError:
        return False
    
def parse_appointment_input(pacient, doctor, date, time):
    if pacient is None or doctor is None or date is None or time is None:
        raise InvalidInput("Missing fields")
    if not is_valid_datetime(date, "%Y-%m-%d"):
        raise InvalidInput("Invalid date format")
    if not is_valid_datetime(time, "%H:%M"):
        raise InvalidInput("Invalid time format")
    
def check_clinic_name(query_result):
    if not query_result:
        raise NonExistentValue("This clinic does not exist")
