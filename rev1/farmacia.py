class Medicamento:
    def __init__(self, nome, farmaceutica, necessita_receita, descricao, observacoes=""):
        self.nome = nome
        self.farmaceutica = farmaceutica
        self.necessita_receita = necessita_receita
        self.descricao = descricao
        self.observacoes = observacoes

    def __str__(self):
        return (f"Medicamento(Nome: {self.nome}, Farmacêutica: {self.farmaceutica}, "
                f"Necessita Receita: {self.necessita_receita}, Descrição: {self.descricao}, "
                f"Observações: {self.observacoes})")


class Farmacia:
    def __init__(self):
        self.estoque = []

    def adicionar_medicamento(self, medicamento):
        self.estoque.append(medicamento)
        print(f"Medicamento {medicamento.nome} adicionado com sucesso!")

    def remover_medicamento(self, nome):
        medicamento = next((med for med in self.estoque if med.nome == nome), None)
        if medicamento:
            self.estoque.remove(medicamento)
            print(f"Medicamento {nome} removido com sucesso!")
        else:
            print("Medicamento não encontrado.")

    def atualizar_medicamento(self, nome, **kwargs):
        medicamento = next((med for med in self.estoque if med.nome == nome), None)
        if medicamento:
            if 'farmaceutica' in kwargs:
                medicamento.farmaceutica = kwargs['farmaceutica']
            if 'necessita_receita' in kwargs:
                medicamento.necessita_receita = kwargs['necessita_receita']
            if 'descricao' in kwargs:
                medicamento.descricao = kwargs['descricao']
            if 'observacoes' in kwargs:
                medicamento.observacoes = kwargs['observacoes']
            print(f"Medicamento {nome} atualizado com sucesso!")
        else:
            print("Medicamento não encontrado.")

    def visualizar_medicamentos(self):
        if not self.estoque:
            print("Nenhum medicamento no estoque.")
        else:
            return [str(med) for med in self.estoque]


