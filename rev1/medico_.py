class Medico:
    _id_counter = 1

    def __init__(self, nome, data_nascimento, telefone, email, especialidade=None, CRM=None, departamento=None):
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
        self.feedbacks = []
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
        print(f"Consulta adicionada: {consulta.descricao}")

    def remover_consulta(self, consulta):
        if consulta in self.consultas:
            self.consultas.remove(consulta)
            print(f"Consulta removida: {consulta.descricao}")

    def atualizar_consulta(self, consulta, nova_descricao=None, nova_data=None, novo_departamento=None):
        if nova_descricao:
            consulta.descricao = nova_descricao
        if nova_data:
            consulta.data = nova_data
        if novo_departamento:
            consulta.departamento = novo_departamento
        print(f"Consulta atualizada: {consulta}")

    def visualizar_consultas(self):
        return [str(consulta) for consulta in self.consultas]

    def adicionar_cirurgia(self, cirurgia):
        self.cirurgias.append(cirurgia)
        print(f"Cirurgia adicionada: {cirurgia.descricao}")

    def remover_cirurgia(self, cirurgia):
        if cirurgia in self.cirurgias:
            self.cirurgias.remove(cirurgia)
            print(f"Cirurgia removida: {cirurgia.descricao}")

    def atualizar_cirurgia(self, cirurgia, nova_descricao=None, nova_data=None, novo_departamento=None):
        if nova_descricao:
            cirurgia.descricao = nova_descricao
        if nova_data:
            cirurgia.data = nova_data
        if novo_departamento:
            cirurgia.departamento = novo_departamento
        print(f"Cirurgia atualizada: {cirurgia}")

    def adicionar_observacao_cirurgia(self, cirurgia, observacao):
        if cirurgia in self.cirurgias:
            cirurgia.adicionar_observacao(observacao)
        else:
            print("Cirurgia não encontrada.")

    def atualizar_resultado_cirurgia(self, cirurgia, resultado):
        if cirurgia in self.cirurgias:
            cirurgia.atualizar_resultado(resultado)
        else:
            print("Cirurgia não encontrada.")

    def visualizar_cirurgias(self):
        return [str(cirurgia) for cirurgia in self.cirurgias]


    def prescrever_medicamento(self, paciente, medicamento, observacao):
        paciente.adicionar_medicamento_prescrito(medicamento, observacao)
        print(f"Medicamento {medicamento.nome} prescrito para {paciente.nome} com observação: {observacao}")
