
from src.Usuario import Usuario


class Sistema:

    def __init__(self):
        self.usuarios = []
        self.usuario_logado = self.login()
        # self.menu_principal = menu_principal

    def cadastrar_conta(self):
        nome = input("Nome: ")
        email = input("Email: ")
        senha = input("Senha: ")
        idade = int(input("Idade: "))

        usuario = Usuario(nome, email, idade, senha)
        self.usuarios.append(usuario)
        return usuario

    def remover_conta(self, usuario_logado):
        self.usuarios.remove(usuario_logado)
        exit()

    @staticmethod
    def listar_usuarios(self):
        for usuario in self.usuarios:
            print(usuario)

    def menu(self):
        while True:
            print("\n1. Remover conta"
                  "\n2. Mudar status"
                  "\n3. Mudar apelido"
                  "\n4. Mudar idade"
                  "\n5. Mudar nome"
                  "\n6. Listar usuários")
            resposta = int(input(": "))

            if resposta == 1:  # Remover conta
                self.remover_conta(self.usuario_logado)
            elif resposta == 2:  # Mudar status
                novo_status = input('Status: ')
                self.usuario_logado.set_status(novo_status)
            elif resposta == 3:  # Mudar apelido
                novo_apelido = input('Apelido: ')
                self.usuario_logado.set_apelido(novo_apelido)
            elif resposta == 4:  # Mudar idade
                nova_idade = int(input('Idade: '))
                self.usuario_logado.set_idade(nova_idade)
            elif resposta == 5:  # Mudar nome
                novo_nome = input('Nome: ')
                self.usuario_logado.set_nome(novo_nome)
            elif resposta == 6:  # Listar usuario
                self.listar_usuarios()
            else:
                print("Opção inválida!")

    def login(self):
        tem_conta = input("Tens conta? (s/n): ")

        if tem_conta == "s":
            email = input("Email: ")
            senha = input("Senha: ")

            for usuario in self.usuarios:
                if usuario.email == email and usuario.senha == senha:
                    return usuario
        else:
            deseja_ter_conta = input("Desejas uma? (s/n): ")

            if deseja_ter_conta == "s":
                return self.cadastrar_conta()
            else:
                exit()


