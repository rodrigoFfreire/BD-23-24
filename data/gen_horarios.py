from datetime import timedelta, date, time, datetime

def create_table():
    return \
"""TRUNCATE possible_schedules RESTART IDENTITY;

CREATE TABLE IF NOT EXISTS possible_schedules(
    data DATE NOT NULL,
    hora TIME NOT NULL
);\n
"""

def date_range(start: date, stop: date, step: timedelta):
    current = start
    while current <= stop:
        yield current
        current += step

def time_range(start: time, stop: time, step: timedelta):
    start = datetime.combine(datetime.today(), start)
    stop = datetime.combine(datetime.today(), stop)
    current = start

    while current <= stop:
        yield current.time()
        if current.time() == time(12, 30):
            current += timedelta(minutes=90)
        else:
            current += step

def populate():
    out = []

    out.append(create_table())

    out.append("INSERT INTO possible_schedules VALUES\n")
    for d in date_range(date(2024, 6, 1), date(2024, 12, 31), timedelta(days=1)):
        for h in time_range(time(8, 0), time(18, 30), timedelta(minutes=30)):
            out.append(f"('{d}', '{h}')")
            out.append(',\n')
    
    out = out[:-1]
    out.append(";")

    return "".join(out)


with open('./horarios.sql', 'w') as f:
    f.write(populate())