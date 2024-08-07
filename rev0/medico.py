class Medico:
    _id_counter = 1

    def __init__(self, nome, data_nascimento, telefone, email, especialidade, CRM, departamento=None):
        self.id = Medico._generate_id()
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.telefone = telefone
        self.email = email
        self.especialidade = especialidade
        self.CRM = CRM
        self.departamento = departamento
        self.consultas = []
        self.cirurgias = []
        self.tratamentos = []
        self.feedback = []
        self.exames = []

    @classmethod
    def _generate_id(cls):
        current_id = cls._id_counter
        cls._id_counter += 1
        return current_id

    def __str__(self):
        return (f"Médico(ID: {self.id}, Nome: {self.nome}, Data de Nascimento: {self.data_nascimento}, "
                f"Telefone: {self.telefone}, Email: {self.email}, Especialidade: {self.especialidade}, "
                f"CRM: {self.CRM}, Departamento: {self.departamento.nome if self.departamento else 'Nenhum'})")

    def adicionar_consulta(self, consulta):
        self.consultas.append(consulta)

    def atualizar_consulta(self, consulta_id, novos_dados):
        self.consultas[consulta_id] = novos_dados

    def cancelar_consulta(self, consulta_id):
        self.consultas.pop(consulta_id)

    def visualizar_consultas(self):
        return self.consultas

    def adicionar_cirurgia(self, cirurgia):
        self.cirurgias.append(cirurgia)

    def atualizar_cirurgia(self, cirurgia_id, novos_dados):
        self.cirurgias[cirurgia_id] = novos_dados

    def visualizar_cirurgias(self):
        return self.cirurgias

    def adicionar_tratamento(self, tratamento):
        self.tratamentos.append(tratamento)

    def atualizar_tratamento(self, tratamento_id, novos_dados):
        self.tratamentos[tratamento_id] = novos_dados

    def visualizar_tratamentos(self):
        return self.tratamentos

    def visualizar_pacientes(self):
        pacientes = []
        for consulta in self.consultas:
            if consulta.paciente not in pacientes:
                pacientes.append(consulta.paciente)
        for cirurgia in self.cirurgias:
            if cirurgia.paciente not in pacientes:
                pacientes.append(cirurgia.paciente)
        for tratamento in self.tratamentos:
            if tratamento.paciente not in pacientes:
                pacientes.append(tratamento.paciente)
        return pacientes
