
from src.Usuario import Usuario


class Sistema:

    def __init__(self):
        self.usuarios = []
        self.usuario_logado = self.login()
        self.mostrar_menu()

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

    def listar_usuarios(self):
        for usuario in self.usuarios:
            print(usuario)

    def mostrar_menu(self):

        while True:
            opcao = input('\n\tmenu principal:\n'
                          'U usuarios\n'
                          '> ')
            if opcao == 'U':

                while True:
                    opcao = input('\n\tusuarios:\n'
                                  'l listar\n'
                                  '> ')
                    if opcao == 'l':
                        self.listar_usuarios()
                    elif opcao == '\\':
                        break

            elif opcao == '\\':
                print('nenhum menu acima deste')

            else:
                print('opção inválida')

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
