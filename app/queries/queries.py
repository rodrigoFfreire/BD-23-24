# Lists all available clinics
LIST_CLINICS = \
    """SELECT nome, morada
    FROM clinica;
    """

# Lists all specialties given a clinic
LIST_SPECIALTIES = \
    """
    SELECT DISTINCT m.especialidade
    FROM medico m
    JOIN trabalha t ON m.nif = t.nif
    JOIN clinica c ON t.nome = c.nome
    WHERE c.nome = %(clinic_name)s;
    """

# Lists all doctors (nif) with a given specialty and clinic 
LIST_SPECIALTY_DOCTORS = \
    """
    SELECT DISTINCT m.nome, m.nif
    FROM medico m
    JOIN trabalha t ON m.nif = t.nif
    WHERE t.nome = %(clinic_name)s AND m.especialidade = %(specialty)s; 
    """

# Fetches the date and time of all appointments of a doctor in a clinic 
LIST_DOCTOR_SCHEDULES = \
    """
    SELECT t1.data, t1.hora
    FROM (
        SELECT data, hora
        FROM possible_schedules
        WHERE check_if_doctor_works(data, %(clinic_name)s, %(doctor_nif)s) = TRUE
    ) t1
    LEFT JOIN (
        SELECT data, hora
        FROM consulta
        WHERE nome = %(clinic_name)s
            AND nif = %(doctor_nif)s
            AND (data > CURRENT_DATE OR (data = CURRENT_DATE AND hora > CURRENT_TIME)) 
    ) t2 ON t1.data = t2.data AND t1.hora = t2.hora
    WHERE t2.data IS NULL
    ORDER BY t1.data, t1.hora;
    """

# Checks if the specified clinic exists in the database
CHECK_CLINIC = \
    """
    SELECT check_args(%(clinic_name)s);
    """

# Checkf is we can schedule an appointment with the given arguments
# Otherwise raises Exception
SCHEDULE_APPOINTMENT = \
    """
    SELECT schedule_appointment(%(clinic_name)s, %(pacient_ssn)s, %(doctor_nif)s, %(date)s, %(time)s)
    """

# Checks if an appointment with provided clinic, pacient, doctor and date & time exists and cancels (deletes)
# Otherwise raises Exception
DELETE_APPOINTMENT = \
    """
    SELECT delete_appointment(%(clinic_name)s, %(pacient_ssn)s, %(doctor_nif)s, %(date)s, %(time)s)
    """