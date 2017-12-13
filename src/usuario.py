
class Usuario:

    def __init__(self, nome, email, idade, senha, status='', apelido=''):
        self.nome = nome
        self.email = email
        self.idade = idade
        self.senha = senha
        self.status = status
        self.apelido = apelido

    def set_status(self, status):
        self.status = status

    def set_idade(self, idade):
        if idade > 0:
            self.idade = idade

    def set_apelido(self, apelido):
        self.apelido = apelido

    def set_nome(self, nome):
        if len(nome) > 0:
            self.nome = nome

    def get_email(self):
        return self.email

    def get_senha(self):
        return self.senha



