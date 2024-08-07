from medico_ import *
from especialidade_ import *
from consulta import *
from cirurgias import *
from paciente import *
from feedback import *
from farmacia import *

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
            print(f"Médico {medico.nome} adicionado ao departamento {self.nome} com sucesso!")

    def remover_medico(self, medico):
        if medico in self.medicos:
            self.medicos.remove(medico)
            medico.departamento = None
            print(f"Médico {medico.nome} removido do departamento {self.nome} com sucesso!")

    def listar_medicos(self):
        return [medico.nome for medico in self.medicos]


