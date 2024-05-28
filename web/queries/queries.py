# Lists all available clinics
LIST_CLINICS_QUERY = \
    """SELECT nome, morada
    FROM clinica;
    """

# Searches for a specific clinic's name. Returns [] if not found  
FIND_CLINIC_QUERY = \
    """
    SELECT nome
    FROM clinica
    WHERE nome = %(clinic_name)s;
    """

# Lists all specialties given a clinic
LIST_SPECIALTIES_QUERY = \
    """
    SELECT DISTINCT m.especialidade
    FROM medico m
    JOIN trabalha t ON m.nif = t.nif
    JOIN clinica c ON t.nome = c.nome
    WHERE c.nome = %(clinic_name)s;
    """

# Lists all doctor with a given specialty and clinic  
LIST_SPECIALTY_DOCTORS_QUERY = \
    """
    SELECT m.nome
    FROM medico m
    JOIN trabalha t ON m.nif = t.nif
    JOIN clinica c ON t.nome = c.nome
    WHERE c.nome = %(clinic_name)s AND m.especialidade = %(specialty)s; 
    """

# Fetches the date and time of all appointments of a doctor 
LIST_DOCTOR_SCHEDULES_QUERY = \
    """
    SELECT c.data, c.hora
    FROM consulta c
    JOIN medico m ON c.nif = m.nif
    WHERE m.nome = %(doctor_name)s
        AND c.data > CURRENT_DATE
        OR (c.data = CURRENT_DATE AND c.hora > CURRENT_TIME);
    """
    
# Deletes appointment given pacient, doctor, clinic and date & time
DELETE_APPOINTMENT_QUERY = \
    """
    DELETE FROM consulta c
    USING paciente p, medico m
    JOIN p ON c.SSN = p.SSN
    JOIN m ON c.NIF = m.NIF
    WHERE c.nome = %(clinic_name)s
        AND c.data = %(data)s
        AND c.hora = %(hora)s
        AND p.nome = %(pacient_name)s
        AND m.nome = %(doctor_name)s;
    """
