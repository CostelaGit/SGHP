class Consulta:
    def __init__(self, medico, departamento, paciente, data, descricao):
        self.medico = medico
        self.departamento = departamento
        self.paciente = paciente
        self.data = data
        self.descricao = descricao

    def __str__(self):
        return (f"Consulta(Médico: {self.medico.nome}, Departamento: {self.departamento.nome}, "
                f"Paciente: {self.paciente.nome}, Data: {self.data}, Descrição: {self.descricao})")
