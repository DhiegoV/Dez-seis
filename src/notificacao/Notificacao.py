
class Notificacao:

    def __init__(self, rementente, destinatario, mensagem):
        self.remetente = rementente
        self.destinatario = destinatario
        self.mensagem = mensagem

    def __str__(self):
        return self.mensagem

    def get_remetente(self):
        return self.remetente

    def get_destinatario(self):
        return self.destinatario

    def get_mensagem(self):
        return self.mensagem
