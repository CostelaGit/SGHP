class Feedback:
    def __init__(self, paciente, cirurgia, comentario):
        self.paciente = paciente
        self.cirurgia = cirurgia
        self.comentario = comentario

    def __str__(self):
        return (f"Feedback(Paciente: {self.paciente.nome}, Cirurgia: {self.cirurgia.descricao}, "
                f"Médico: {self.cirurgia.medico.nome}, Departamento: {self.cirurgia.departamento.nome}, "
                f"Comentário: {self.comentario})")

    def atualizar_comentario(self, novo_comentario):
        self.comentario = novo_comentario
        print(f"Comentário atualizado: {novo_comentario}")

    def visualizar_feedback(self):
        return str(self)
    
class GestorFeedback:
    def __init__(self):
        self.feedbacks = []

    def adicionar_feedback(self, feedback):
        self.feedbacks.append(feedback)
        print(f"Feedback adicionado: {feedback}")

    def remover_feedback(self, feedback):
        if feedback in self.feedbacks:
            self.feedbacks.remove(feedback)
            print(f"Feedback removido: {feedback}")
        else:
            print("Feedback não encontrado.")

    def atualizar_feedback(self, feedback, novo_comentario):
        if feedback in self.feedbacks:
            feedback.atualizar_comentario(novo_comentario)
        else:
            print("Feedback não encontrado.")

    def visualizar_feedbacks(self):
        if not self.feedbacks:
            print("Nenhum feedback disponível.")
        else:
            return [str(feedback) for feedback in self.feedbacks]

