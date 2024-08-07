class Cirurgia:
    def __init__(self, medico, departamento, data, descricao):
        self.medico = medico
        self.departamento = departamento
        self.data = data
        self.descricao = descricao
        self.observacoes = []
        self.resultado = None

    def adicionar_observacao(self, observacao):
        self.observacoes.append(observacao)
        print(f"Observação adicionada: {observacao}")

    def atualizar_resultado(self, resultado):
        self.resultado = resultado
        print(f"Resultado atualizado: {resultado}")

    def visualizar_observacoes(self):
        return self.observacoes

    def visualizar_resultado(self):
        return self.resultado

    def __str__(self):
        return (f"Cirurgia(Descrição: {self.descricao}, Médico: {self.medico.nome}, "
                f"Departamento: {self.departamento.nome}, Data: {self.data}, "
                f"Observações: {self.observacoes}, Resultado: {self.resultado})")
