class Especialidades:
    def __init__(self):
        self.especialidades = {}

    def adicionar_especialidade(self, especialidade, medico):
        if especialidade not in self.especialidades:
            self.especialidades[especialidade] = []
        if medico not in self.especialidades[especialidade]:
            self.especialidades[especialidade].append(medico)
            medico.especialidade = especialidade
            print(f"Especialidade {especialidade} adicionada para o médico {medico.nome} com sucesso!")

    def remover_especialidade(self, especialidade, medico):
        if especialidade in self.especialidades and medico in self.especialidades[especialidade]:
            self.especialidades[especialidade].remove(medico)
            if not self.especialidades[especialidade]:  # Remove a especialidade se não houver médicos
                del self.especialidades[especialidade]
            medico.especialidade = None
            print(f"Especialidade {especialidade} removida do médico {medico.nome} com sucesso!")

    def atualizar_especialidade(self, medico, nova_especialidade):
        antiga_especialidade = medico.especialidade
        if antiga_especialidade:
            self.remover_especialidade(antiga_especialidade, medico)
        self.adicionar_especialidade(nova_especialidade, medico)

    def visualizar_especialidades(self):
        return {especialidade: [medico.nome for medico in medicos] for especialidade, medicos in self.especialidades.items()}

    def listar_medicos_por_especialidade(self, especialidade):
        if especialidade in self.especialidades:
            return [medico.nome for medico in self.especialidades[especialidade]]
        else:
            print(f"Especialidade {especialidade} não encontrada.")
            return []
