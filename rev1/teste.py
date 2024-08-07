from departamento_ import *

# Criação de departamentos
departamento_cardiologia = Departamento("Cardiologia", "Ala A")
departamento_ortopedia = Departamento("Ortopedia", "Ala B")

# Criação da instância de Especialidades
especialidades = Especialidades()

# Criação de médicos
medico1 = Medico("Dr. João", "01/01/1980", "123456789", "joao@example.com", "Cardiologia", "12345", departamento_cardiologia)
medico2 = Medico("Dra. Maria", "02/02/1985", "987654321", "maria@example.com", "Ortopedia", "67890", departamento_ortopedia)

# Adicionando médicos aos departamentos
departamento_cardiologia.adicionar_medico(medico1)
departamento_ortopedia.adicionar_medico(medico2)

# Adicionando especialidades aos médicos
especialidades.adicionar_especialidade("Cardiologia", medico1)
especialidades.adicionar_especialidade("Ortopedia", medico2)

# Criação de pacientes
paciente1 = Paciente("Carlos Silva", "10/10/1990", "111222333", "carlos@example.com")
paciente2 = Paciente("Ana Souza", "20/20/1995", "444555666", "ana@example.com")

# Criação de consultas
consulta1 = Consulta(medico1, departamento_cardiologia, paciente1, "15/03/2023", "Consulta inicial")
consulta2 = Consulta(medico2, departamento_ortopedia, paciente2, "16/03/2023", "Consulta de avaliação")

# Adicionando consultas aos pacientes
paciente1.adicionar_consulta(consulta1)
paciente2.adicionar_consulta(consulta2)

# Criação de cirurgias
cirurgia1 = Cirurgia(medico1, departamento_cardiologia, "20/03/2023", "Cirurgia cardíaca")
cirurgia2 = Cirurgia(medico2, departamento_ortopedia, "21/03/2023", "Cirurgia ortopédica")

# Adicionando cirurgias aos pacientes
paciente1.adicionar_cirurgia(cirurgia1)
paciente2.adicionar_cirurgia(cirurgia2)

# Adicionando observações e resultados às cirurgias
medico1.adicionar_observacao_cirurgia(cirurgia1, "Paciente respondeu bem à anestesia.")
medico1.atualizar_resultado_cirurgia(cirurgia1, "Cirurgia bem-sucedida, paciente em recuperação.")

medico2.adicionar_observacao_cirurgia(cirurgia2, "Cirurgia realizada com sucesso, sem complicações.")
medico2.atualizar_resultado_cirurgia(cirurgia2, "Paciente estável e em recuperação.")

# Visualização das observações e resultados das cirurgias
print(paciente1.visualizar_observacoes_cirurgia(cirurgia1))
print(paciente1.visualizar_resultado_cirurgia(cirurgia1))

print(paciente2.visualizar_observacoes_cirurgia(cirurgia2))
print(paciente2.visualizar_resultado_cirurgia(cirurgia2))

# Visualizando o histórico médico dos pacientes
print(paciente1.historico_medico())
print(paciente2.historico_medico())

print("\n"
      "\n")

# Criação da instância da Farmacia
farmacia = Farmacia()

# Criação de medicamentos
medicamento1 = Medicamento("Aspirina", "Farmaceutica A", True, "Uso para dor de cabeça e febre")
medicamento2 = Medicamento("Ibuprofeno", "Farmaceutica B", True, "Uso para dor e inflamação")

# Adicionando medicamentos à farmácia
farmacia.adicionar_medicamento(medicamento1)
farmacia.adicionar_medicamento(medicamento2)

# Atualizando um medicamento
farmacia.atualizar_medicamento("Aspirina", descricao="Uso para dor e febre")

# Visualizando medicamentos na farmácia
print("Medicamentos na farmácia:")
for med in farmacia.visualizar_medicamentos():
    print(med)

# Prescrevendo medicamentos para pacientes
medico1.prescrever_medicamento(paciente1, medicamento1, "Tomar 1 comprimido a cada 6 horas")
medico2.prescrever_medicamento(paciente2, medicamento2, "Tomar 2 comprimidos a cada 8 horas")

# Visualizando medicamentos prescritos pelos pacientes
print("Medicamentos prescritos para Carlos Silva:")
for med in paciente1.visualizar_medicamentos_prescritos():
    print(med)

print("Medicamentos prescritos para Ana Souza:")
for med in paciente2.visualizar_medicamentos_prescritos():
    print(med)
