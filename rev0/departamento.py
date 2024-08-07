from medico import *
from especialidade import *

# departamento

class Departamento:
    def __init__(self, nome, localizacao):
        self.nome = nome
        self.localizacao = localizacao
        self.medicos = []
        self.enfermeiros = []
        self.consultas = []
        self.procedimentos = []
        self.recursos_equipamentos = []

    def adicionar_medico(self, medico):
        if medico not in self.medicos:
            self.medicos.append(medico)
            medico.departamento = self
            print("Médico adicionado com sucesso!")

    def remover_medico(self, medico):
        if medico in self.medicos:
            self.medicos.remove(medico)
            medico.departamento = None
            print("Médico removido com sucesso!")

    def listar_medicos(self):
        return [medico.nome for medico in self.medicos]
    
    def adicionar_enfermeiro(self, enfermeiro):
        if enfermeiro not in self.enfermeiros:
            self.enfermeiros.append(enfermeiro)
            enfermeiro.departamento = self
            print("Enfermeiro adicionado com sucesso!")

    def remover_enfermeiro(self, enfermeiro):
        if enfermeiro in self.enfermeiros:
            self.enfermeiros.remove(enfermeiro)
            enfermeiro.departamento = None
            print("Enfermeiro removido com sucesso!")

    def listar_enfermeiros(self):
        return [enfermeiro.nome for enfermeiro in self.enfermeiros]
    
    def adicionar_consulta(self, consulta):
        if consulta not in self.consultas:
            self.consultas.append(consulta)
            consulta.departamento = self
            print("Consulta adicionada com sucesso!")

    def listar_consultas(self):
        return [consulta.data for consulta in self.consultas]
    
    def adicionar_procedimento(self, procedimento):
        if procedimento not in self.procedimentos:
            self.procedimentos.append(procedimento)
            procedimento.departamento = self
            print("Procedimento adicionado com sucesso!")

    def listar_procedimentos(self):
        return [procedimento.nome for procedimento in self.procedimentos]
    
    def adicionar_recurso_equipamento(self, recurso_equipamento):
        if recurso_equipamento not in self.recursos_equipamentos:
            self.recursos_equipamentos.append(recurso_equipamento)
            recurso_equipamento.departamento = self
            print("Recurso/equipamento adicionado com sucesso!")