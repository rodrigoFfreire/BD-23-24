import random
import datetime

# 100 first and last names
primeiros_nomes = ['Isabela', 'Lucas', 'César', 'Mafalda', 'Tomé', 'Adriana', 'Sandro', 'Pilar', 'Bryan', 'Artur', 'Núria', 'Diogo', 'Cristiano', 'Gaspar', 'José', 'Ivo', 'Carlos', 'Ivan', 'Helena', 'Sofia', 'Eduarda', 'Salomé', 'Mélanie', 'Afonso', 'Leandro', 'Fabiana', 'Juliana', 'Rafael', 'Mara', 'Larissa', 'Kévim', 'Luísa', 'Violeta', 'Joaquim', 'Ângelo', 'Alexandra', 'David', 'Erika', 'Miguel', 'Maria', 'Gonçalo', 'Simão', 'Patrícia', 'Pedro', 'Duarte', 'Nelson', 'Débora', 'Benjamim', 'Leonardo', 'Sara', 'Francisca', 'Erica', 'Lara', 'Miriam', 'Bernardo', 'Carolina', 'Isaac', 'Leonor', 'Júlia', 'Marco', 'Lorena', 'Margarida', 'Ismael', 'Bárbara', 'Kevin', 'Rúben', 'Laura', 'Caetana', 'Paulo', 'Marcos', 'Emília', 'Nádia', 'William', 'Vasco', 'Naiara', 'Tatiana', 'Filipe', 'Beatriz', 'Noa', 'Joel', 'Eduardo', 'Alice', 'Bruno', 'Kyara', 'Flor', 'Daniel', 'Edgar', 'Luís', 'Rodrigo', 'Renato']
ultimos_nomes = ['Reis', 'Magalhães', 'Freitas', 'Azevedo', 'Machado', 'Sousa', 'Nascimento', 'Pinto', 'Domingues', 'Santos', 'Fonseca', 'Ribeiro', 'Alves', 'Figueiredo', 'Gaspar', 'Abreu', 'Vieira', 'Vaz', 'Lourenço', 'Coelho', 'Cunha', 'Miranda', 'Torres', 'Moreira', 'Rodrigues', 'Soares', 'Henriques', 'Andrade', 'Fernandes', 'Melo', 'Amaral', 'Oliveira', 'Silva', 'Lopes', 'Neves', 'Matos', 'Simões', 'Rocha', 'Carneiro', 'Gonçalves', 'Moura', 'Macedo', 'Mendes', 'Pereira', 'Ferreira', 'Castro', 'Neto', 'Valente', 'Pacheco', 'Esteves', 'Nunes', 'Carvalho', 'Maia', 'Loureiro', 'Morais', 'Mota', 'Borges', 'Marques', 'Guerreiro', 'Anjos', 'Sá', 'Paiva', 'Monteiro', 'Jesus', 'Ramos', 'Cardoso', 'Teixeira', 'Leal', 'Assunção', 'Costa', 'Matias', 'Branco', 'Almeida', 'Antunes', 'Leite', 'Campos', 'Pinheiro', 'Pinho', 'Garcia', 'Barros', 'Barbosa', 'Brito', 'Gomes', 'Pires', 'Faria', 'Araújo', 'Cruz', 'Baptista', 'Amorim', 'Martins']

# Combine names
nomes = [f"{primeiro} {ultimo}" for primeiro in primeiros_nomes for ultimo in ultimos_nomes]

nif = 200000000
telefone = 212000000

# 20 Clinica geral + 40 Outras especialidades
especialidades = [
  # 20 Here
  {"nome": "Clínica geral", "num_medicos": 20},
  # 40 Here
  {"nome": "Cardiologia", "num_medicos": 10},
  {"nome": "Ortopedia", "num_medicos": 8},
  {"nome": "Oftalmologia", "num_medicos": 9},
  {"nome": "Neurologia", "num_medicos": 7},
  {"nome": "Urologia", "num_medicos": 6},
]

# 50 Sintomas quantitativos
sintomas_qualitativos = [
    "Febre",
    "Dor de cabeça",
    "Náuseas",
    "Vómitos",
    "Fadiga",
    "Diarreia",
    "Tosse",
    "Falta de ar",
    "Dor no peito",
    "Tonturas",
    "Dor de garganta",
    "Dores musculares",
    "Dor nas articulações",
    "Dor abdominal",
    "Obstipação",
    "Batimento cardíaco rápido",
    "Inchaço",
    "Erupção cutânea",
    "Comichão",
    "Dificuldade em engolir",
    "Perda de peso",
    "Ganho de peso",
    "Perda de apetite",
    "Sede excessiva",
    "Micção frequente",
    "Sangue na urina",
    "Sangue nas fezes",
    "Alterações na visão",
    "Perda auditiva",
    "Epistaxis",
    "Suores noturnos",
    "Calafrios",
    "Pele pálida",
    "Icterícia",
    "Dificuldade em dormir",
    "Perda de memória",
    "Confusão",
    "Alterações de humor",
    "Ansiedade",
    "Depressão",
    "Alucinações",
    "Paralisia",
    "Dormência ou formigamento",
    "Tremores",
    "Convulsões",
    "Desmaio",
    "Hematomas ou sangramentos inexplicados",
    "Menstruação irregular",
    "Disfunção erétil",
    "Perda de libido"
]

# 20 observacoes metricas
observacoes_metricas = [
  {"sintoma": "Frequência Cardíaca", "avg": 100, "std_dev": 20},
  {"sintoma": "Pressão Arterial Sistólica", "avg": 120, "std_dev": 10},
  {"sintoma": "Pressão Arterial Diastólica", "avg": 80, "std_dev": 2},
  {"sintoma": "Taxa Respiratória", "avg": 14, "std_dev": 1},
  {"sintoma": "Temperatura Corporal", "avg": 37, "std_dev": 0.5},
  {"sintoma": "Saturação de Oxigênio no Sangue", "avg": 99, "std_dev": 0.3},
  {"sintoma": "Glicemia", "avg": 100, "std_dev": 10},
  {"sintoma": "Taxa de Sudorese", "avg": 1, "std_dev": 0.4},
  {"sintoma": "Dilatação Pupilar", "avg": 5, "std_dev": 0.2},
  {"sintoma": "Capacidade Pulmonar", "avg": 4, "std_dev": 0.6},
  {"sintoma": "Hemoglobina", "avg": 14, "std_dev": 0.5},
  {"sintoma": "Hematócrito", "avg": 42, "std_dev": 2},
  {"sintoma": "Leucocitos", "avg": 7, "std_dev": 1.5},
  {"sintoma": "Eritrocitos", "avg": 4, "std_dev": 0.2},
  {"sintoma": "Albumina", "avg": 3.9, "std_dev": 0.2},
  {"sintoma": "Bilirrubina", "avg": 1, "std_dev": 0.2},
  {"sintoma": "Fosfatase alcalina", "avg": 80, "std_dev": 5},
  {"sintoma": "Ácido Úrico", "avg": 4, "std_dev": 0.5},
  {"sintoma": "Colesterol (Total)", "avg": 180, "std_dev": 30},
  {"sintoma": "Densidade Mineral Óssea", "avg": 1, "std_dev": 0.1},
]

# 6 medicamentos
medicamentos = ["Paracetamol", "Ibuprofeno", "Metoprolol", "Hidrocortisona", "Difenidramina", "Pseudoefedrina"]

# Usado para gerar o doente crónico (paciente[0], ssn: 10000000000) para a 5.3 dar resultados...
cardiologistas_nifs = []
receitas_paciente0 = []

def dict_to_sql(table_name, data):
  """Converts a list of dictionaries of the same type 
  to a list of SQL INSERT statements."""
  statement = [
    f"INSERT INTO {table_name} ({', '.join(data[0].keys())}) VALUES"
  ]
  for row in data:
    values = ', '.join([f"'{value}'" if value != 'NULL' else 'NULL' for value in row.values()])
    statement.append(f"({values}),")
  statement[-1] = statement[-1][:-1] + ';'
  return '\n' + '\n'.join(statement)

def write_to_file(filename, sql_statements):
  with open(filename, 'w') as f:
    for line in sql_statements:
      f.write(line + '\n')
      # print(line)

def get_morada():
  return f"Rua {random.randint(1,300)}, {random.randint(1000, 2799)}-{random.randint(100, 999)} {random.choice(['Lisboa', 'Cascais', 'Amadora', 'Odivelas', 'Oeiras'])}"

def date_range(start: datetime.date, stop: datetime.date):
  current = start
  while current <= stop:
    yield current
    current += datetime.timedelta(days=1)

def time_range(start: datetime.time, stop: datetime.time):
  start = datetime.datetime.combine(datetime.datetime.today(), start)
  stop = datetime.datetime.combine(datetime.datetime.today(), stop)
  current = start

  while current <= stop:
    yield current.time()
    if current.time() == datetime.time(12, 30):
      current += datetime.timedelta(minutes=90) # Skips lunch break
    else:
      current += datetime.timedelta(minutes=30)

def gen_next_nif(current_nif: int):
  current_nif += random.randint(69, 6960)

  # NIF control digit
  nif_str = str(current_nif)
  soma = sum([int(digito) * (9 - pos) for pos, digito in enumerate(nif_str)])
  resto = soma % 11
  if resto <= 1:
    control = 0
  else:
    control = 11 - resto

  new_nif = int(nif_str)
  return (new_nif // 10) * 10 + control

def generate_clinicas():
  return [
    {"nome": "Clinica Feliz", "telefone": "211185776", "morada": "Avenida dos Estados Unidos da América, 1700-168 Lisboa"},
    {"nome": "Clinica Saude", "telefone": "211001943", "morada": "Rua António Nobre, 2750-655 Cascais"},
    {"nome": "Clínica Cuidar Mais", "telefone": "211661019", "morada": "Estrada do Seminário, 2614-522 Amadora"},
    {"nome": "Clínica Harmonia", "telefone": "211297811", "morada": "Largo do Senhor Roubado, 2675-533 Odivelas"},
    {"nome": "Clínica Vida Plena", "telefone": "211992477", "morada": "Rua Fábrica da Pólvora de Barcarena, 2730-280 Oeiras"}
]

def generate_enfermeiros(clinicas):
  enfermeiros = []
  global nif
  global telefone
  for clinica in clinicas:
    for i in range(random.randint(5, 6)):
      enfermeiros.append({
        'nif': str(nif),
        'nome': nomes.pop(random.randint(0, len(nomes) - 1)),
        'telefone': str(telefone),
        'morada': get_morada(),
        'nome_clinica': clinica['nome']
      })
      nif = gen_next_nif(nif)
      telefone += random.randint(6, 696)
  return enfermeiros

def generate_medicos(especialidades):
  medicos = []
  global nif
  global telefone
  for esp in especialidades:
    for _ in range(esp['num_medicos']):
      if esp['nome'] == 'Cardiologia': cardiologistas_nifs.append(str(nif))
      medicos.append({
        'nif': str(nif),
        'nome': nomes.pop(random.randint(0, len(nomes) - 1)),
        'telefone': str(telefone),
        'morada': get_morada(),
        'especialidade': esp['nome']
      })
      nif = gen_next_nif(nif)
      telefone += random.randint(6, 696)
  return medicos

def generate_trabalha(medicos, clinicas):
  while True:
    valid = True
    trabalha = []
    for medico in medicos:
      clinicas_medico_sample = random.sample(clinicas, random.randint(2,4))
      clinicas_medico = [random.choice(clinicas_medico_sample)['nome'] for _ in range(7)]
      while len(set(clinicas_medico)) < 2:
        clinicas_medico = [random.choice(clinicas_medico_sample)['nome'] for _ in range(7)]
      for i in range(7):
        trabalha.append({
          'nif': medico['nif'],
          'nome': clinicas_medico[i],
          'dia_da_semana': i+1
        })
    # Verificar que todas as clinicas têm pelo menos 8 médicos a trabalhar nesse dia da semana
    for clinica in clinicas:
      for dia in range(1, 8):
        if len([t for t in trabalha if t['nome'] == clinica['nome'] and t['dia_da_semana'] == dia]) < 8:
          valid = False
          break
        if not valid: 
          break
    if valid:
      break
  return trabalha

def generate_pacientes(num_pacientes):
  pacientes = []
  global nif
  global telefone
  ssn = 10000000000
  for paciente_id in range(1, num_pacientes + 1):
    data_nasc = datetime.date(random.randint(1950, 2006), random.randint(1, 12), random.randint(1, 28)).isoformat()
    pacientes.append({
      'ssn': str(ssn),
      'nif': str(nif),
      'nome': nomes.pop(random.randint(0, len(nomes) - 1)),
      'telefone': str(telefone),
      'morada': get_morada(),
      'data_nasc': data_nasc
    })
    nif = gen_next_nif(nif)
    telefone += random.randint(6, 696)
    ssn += random.randint(69, 696969)
  return pacientes

def generate_consultas(pacientes, trabalha, clinicas):
  consultas = []
  global nif
  global telefone
  consulta_id = 1
  codigo_sns = 00000000000
  start_date = datetime.date(2023, 1, 1)
  end_date = datetime.date(2024, 5, 31)
  current_date = start_date
  while current_date <= end_date:
    pacientes_hoje = pacientes.copy()
    cooldown = False
    for clinica in clinicas:
      dia_da_semana = current_date.weekday() + 1
      medicos_clinica = [t['nif'] for t in trabalha if t['nome'] == clinica['nome'] and t['dia_da_semana'] == dia_da_semana]
      horas = [f'{str(i).zfill(2)}:{j}:00' for i in range(8, 13) for j in ("00", "30")]
      horas += [f'{str(i).zfill(2)}:{j}:00' for i in range(14, 19) for j in ("00", "30")]
      for medico_nif in medicos_clinica:
        # 3 consultas por médico garante que há pelo menos 
        # 21 consultas por dia nesta clínica
        # Add appointment for cronic pacient (pacient[0]) (tem que ser consulta de cardiologia)
        m = 0
        for hora in random.sample(horas, random.randint(3, 12)):
          if medico_nif in cardiologistas_nifs and not cooldown:
            consultas.append({
              'id': consulta_id,
              'ssn': pacientes_hoje.pop(0)['ssn'],
              'nif': medico_nif,
              'nome': clinica['nome'],
              'data': current_date.isoformat(),
              'hora': hora,
              'codigo_sns': str(codigo_sns).zfill(12)
            })
            receitas_paciente0.append(str(codigo_sns).zfill(12))
            cooldown = True
            m += 1
          else:
            consultas.append({
              'id': consulta_id,
              'ssn': pacientes_hoje.pop(random.randint(m, len(pacientes_hoje) - 1))['ssn'],
              'nif': medico_nif,
              'nome': clinica['nome'],
              'data': current_date.isoformat(),
              'hora': hora,
              'codigo_sns': str(codigo_sns).zfill(12)
            })
          consulta_id += 1
          codigo_sns += random.randint(1, 6969)
    current_date += datetime.timedelta(days=1)
    cooldown = False
  return consultas


def generate_receitas(consultas):
  receitas = []
  for consulta in consultas:
    if random.random() < 0.8:
      if consulta['codigo_sns'] in receitas_paciente0:
        receitas.append({
          'codigo_sns': consulta['codigo_sns'],
          'medicamento': 'Metoprolol',
          'quantidade': random.randint(1, 3)
        })
        continue

      for medicamento in random.sample(medicamentos, random.randint(1, 6)):
        receitas.append({
          'codigo_sns': consulta['codigo_sns'],
          'medicamento': medicamento,
          'quantidade': random.randint(1, 3)
        })
    else: 
      consulta['codigo_sns'] = 'NULL'
  return receitas

def generate_observacoes(consultas):
  observacoes = []
  for consulta in consultas:
    # 1 a 5 sintomas qualitativos
    for sintoma in random.sample(sintomas_qualitativos, random.randint(1, 5)):
      observacoes.append({
        'id': consulta['id'],
        'parametro': sintoma,
        'valor': 'NULL'
      })
    # 0 a 3 sintomas quantitativos
    for sintoma in random.sample(observacoes_metricas, random.randint(0, 3)):
      valor = random.normalvariate(sintoma['avg'], sintoma['std_dev'])
      observacoes.append({
        'id': consulta['id'],
        'parametro': sintoma['sintoma'],
        'valor': f'{valor:.2f}'
      })
  return observacoes

def generate_possible_schedules():
  possible_schedules = []
  for date in date_range(datetime.date(2024, 6, 1), datetime.date(2024, 12, 31)):
    for time in time_range(datetime.time(8, 0), datetime.time(18, 30)):
      possible_schedules.append({
        'data': f'{date}',
        'hora': f'{time}'
      })
  return possible_schedules

def main():
  sql_statements = [
    "TRUNCATE TABLE receita, observacao, consulta, trabalha, paciente, medico, enfermeiro, clinica RESTART IDENTITY;"
  ]
  clinicas = generate_clinicas()
  medicos = generate_medicos(especialidades)
  enfermeiros = generate_enfermeiros(clinicas)
  trabalha = generate_trabalha(medicos, clinicas)
  pacientes = generate_pacientes(5000)
  consultas = generate_consultas(pacientes, trabalha, clinicas)
  receitas = generate_receitas(consultas)
  observacoes = generate_observacoes(consultas)

  sql_statements.append(dict_to_sql('clinica', clinicas))
  sql_statements.append(dict_to_sql('enfermeiro', enfermeiros))
  sql_statements.append(dict_to_sql('medico', medicos))
  sql_statements.append(dict_to_sql('trabalha', trabalha))
  sql_statements.append(dict_to_sql('paciente', pacientes))
  [c.pop('id') for c in consultas] # Removes manual IDs for appointments because they fuck up the serial sequence
  sql_statements.append(dict_to_sql('consulta', consultas))
  sql_statements.append(dict_to_sql('receita', receitas))
  sql_statements.append(dict_to_sql('observacao', observacoes))

  write_to_file('./populate.sql', sql_statements)

  possible_schedules = generate_possible_schedules()
  schedule_statements = [dict_to_sql('possible_schedules', possible_schedules)]

  write_to_file('./possible_schedules.sql', schedule_statements)

if __name__ == '__main__':
  main()
