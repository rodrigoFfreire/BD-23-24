import random
from faker import Faker

fake = Faker('pt_PT')
with open('LocalidadesLisboa.txt', 'r') as file:
    locations = file.readlines()

with open('ListaEspecialidades.txt', 'r') as file:
    specialties = file.readlines()

# Configurações e dados de exemplo
clinics = ['Germano de Sousa', 'Cruz Vermelha', 'São José', 'Lusiadas', 'Santa Maria']
general_practitioners = 20
other_specialists = 40
patients = 5000
docNIFnum = 60
docNIFs = set()  # use a set to store unique NIFs

while len(docNIFs) < docNIFnum:
    nif = fake.nif()  # generate a Portuguese NIF number
    if nif not in docNIFs:
        docNIFs.add(nif)
        
        
parameters_symptoms = [f'Symptom_{i}' for i in range(1, 51)]
parameters_metrics = [f'Metric_{i}' for i in range(1, 21)]

def chooseSpecialties():
    ans = ['Ortopedia', 'Cardiologia']
    for i in range(3):
        ans.append(random.choice(specialties))
    return ans

def generate_clinics():
    clinic_queries = []
    for clinic in clinics:
        location = random.choice(locations)
        address = fake.address().replace('\n', ', ')
        postal_code = fake.postcode()
        query = f"INSERT INTO clinics (name, address, postal_code, location) VALUES ('{clinic}', '{address}', '{postal_code}', '{location}');"
        clinic_queries.append(query)
    return clinic_queries

def generate_nurses():
    nurse_queries = []
    for clinic in clinics:
        for _ in range(random.randint(5, 6)):
            name = fake.name()
            query = f"INSERT INTO nurses (name, clinic) VALUES ('{name}', '{clinic}');"
            nurse_queries.append(query)
    return nurse_queries

def generate_doctors():
    doctor_queries = []
    doctors = []
    for i in range(general_practitioners):
        name = fake.name()
        specialty = 'Clínica Geral'
        doctors.append((name, specialty))
    special = chooseSpecialties()
    
    
    name = fake.name()
    nif = docNIFs[0
]
    specialty = 'Cardiologia'
    doctors.append((nif, name, specialty))
    
    name = fake.name()
    nif = docNIFs[1
]
    specialty = random.choice('Ortopedia')
    doctors.append((nif, name, specialty))
    
    i=2
    for i in range(other_specialists - 2):
        nif = docNIFs[i
    ]
        name = fake.name()
        specialty = random.choice(special)
        doctors.append((nif, name, specialty))
        i+=1
        
    for nif, name, specialty in doctors:
        query = f"INSERT INTO doctors (nif, name, specialty) VALUES ('{nif}', '{name}', '{specialty}');"
        doctor_queries.append(query)
    return doctor_queries







def assign_day_doctor():
    assignment_queries = []
    """ainda nao testei mas deve estar bem"""
    doc_days = {}
    clinics_done = [[0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]]
    allEigths = False
    
    for i in docNIFs:
        
        placeholder=[0,1,2,3,4]
        num_elements_to_pick = random.randint(2, 5)
        doc_clinics = random.sample(placeholder, num_elements_to_pick)
        lastResort = []
        
        num_working_days = random.randint(num_elements_to_pick, 7)
        days_of_week = [1,2,3,4,5,6,7]
        for i in range(num_working_days):
            if not allEigths:
                if doc_clinics:
                    
                    clinic_choice = random.choice(doc_clinics)
                    day = random.choice(days_of_week)
                    
                    while clinic_choice[day] == 8:
                        clinic_choice = random.choice(doc_clinics)
                        day = random.choice(days_of_week)

                    lastResort.append(clinic_choice)
                    doc_clinics.remove(clinic_choice)
                    num_working_days.remove(day)
                    
                    doc_days[(i,day)] = clinics[clinic_choice]
                    
                else:
                    clinic_choice = random.choice(lastResort)
                    day = random.choice(days_of_week)
                    
                    while clinic_choice[day] == 8:
                        clinic_choice = random.choice(lastResort)
                        day = random.choice(days_of_week)

                    
                    num_working_days.remove(day)
                    
                    doc_days[(i,day)] = clinics[clinic_choice]
                
                allEigths = ((clinics_done[0].count(8) == len(clinics_done[0]) if clinics_done[0] else True) and (clinics_done[1].count(8) == len(clinics_done[1]) if clinics_done[1] else True)and (clinics_done[2].count(8) == len(clinics_done[2]) if clinics_done[2] else True)and (clinics_done[3].count(8) == len(clinics_done[3]) if clinics_done[3] else True)and (clinics_done[4].count(8) == len(clinics_done[4]) if clinics_done[4] else True))
            
            else:
                if doc_clinics:
                    
                    clinic_choice = random.choice(doc_clinics)
                    day = random.choice(days_of_week)

                    lastResort.append(clinic_choice)
                    doc_clinics.remove(clinic_choice)
                    num_working_days.remove(day)
                    
                    doc_days[(i,day)] = clinics[clinic_choice]
                    
                else:
                    clinic_choice = random.choice(lastResort)
                    day = random.choice(days_of_week)
    
                    num_working_days.remove(day)
                    
                    doc_days[(i,day)] = clinics[clinic_choice]
    
    
    for key in doc_days:
        query = f"INSERT INTO clinic_doctor (nif, clinic, day) VALUES ('{key[0]}, {doc_days[key]}', '{key[1]}');"
        assignment_queries.append(query)
            
    return assignment_queries

def generate_patients():
    patient_queries = []
    for _ in range(patients):
        name = fake.name()
        address = fake.address().replace('\n', ', ')
        postal_code = fake.postcode()
        query = f"INSERT INTO patients (name, address, postal_code) VALUES ('{name}', '{address}', '{postal_code}');"
        patient_queries.append(query)
    return patient_queries

def generate_appointments():
    appointment_queries = []
    for _ in range(patients):
        patient_id = random.randint(1, patients)
        doctor_id = random.randint(1, general_practitioners + other_specialists)
        clinic = random.choice(clinics)
        date = fake.date_between(start_date='-1y', end_date='today')
        query = f"INSERT INTO appointments (patient_id, doctor_id, clinic, date) VALUES ({patient_id}, {doctor_id}, '{clinic}', '{date}');"
        appointment_queries.append(query)
    return appointment_queries

def generate_prescriptions():
    prescription_queries = []
    for appointment_id in range(1, patients + 1):
        if random.random() < 0.8:
            medicines = random.randint(1, 6)
            for _ in range(medicines):
                medicine = fake.word()
                quantity = random.randint(1, 3)
                query = f"INSERT INTO prescriptions (appointment_id, medicine, quantity) VALUES ({appointment_id}, '{medicine}', {quantity});"
                prescription_queries.append(query)
    return prescription_queries

def generate_symptom_observations():
    symptom_queries = []
    for appointment_id in range(1, patients + 1):
        symptoms = random.randint(1, 5)
        for _ in range(symptoms):
            symptom = random.choice(parameters_symptoms)
            query = f"INSERT INTO symptom_observations (appointment_id, symptom) VALUES ({appointment_id}, '{symptom}');"
            symptom_queries.append(query)
    return symptom_queries

def generate_metric_observations():
    metric_queries = []
    for appointment_id in range(1, patients + 1):
        metrics = random.randint(0, 3)
        for _ in range(metrics):
            metric = random.choice(parameters_metrics)
            value = round(random.uniform(0.0, 100.0), 2)
            query = f"INSERT INTO metric_observations (appointment_id, metric, value) VALUES ({appointment_id}, '{metric}', {value});"
            metric_queries.append(query)
    return metric_queries

queries = []
queries.extend(generate_clinics())
queries.extend(generate_nurses())
queries.extend(generate_doctors())
queries.extend(assign_doctors_to_clinics())
queries.extend(generate_patients())
queries.extend(generate_appointments())
queries.extend(generate_prescriptions())
queries.extend(generate_symptom_observations())
queries.extend(generate_metric_observations())

for query in queries:
    print(query)