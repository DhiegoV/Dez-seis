from src.usuario import Usuario
from src.ExceptFile3000 import AuthenticationException

class Menu:

    def __init__(self, sistema):
        self.sistema = sistema

    def mostrar_menu_cadastro(self):
        nome = input("Nome: ")
        email = input("Email: ")
        senha = input("Senha: ")
        idade = int(input("Idade: "))
        apelido = input("Apelido: ")

        usuario = Usuario(nome, email, idade, senha, '', apelido)
        self.sistema.cadastrar_conta(usuario)

    def listar_usuarios(self, usuarios):
        print('nomes:')
        for usuario in usuarios:
            print(usuario[0])

    def mostrar_menu_principal(self):
        while True:

            opcao = input('\n\tmenu principal:'
                          '\nC conta'
                          '\nU usuarios'
                          '\nd deslogar'
                          '\n> ')
            if opcao == 'C':
                self.mostrar_menu_conta()
            elif opcao == 'U':
                self.mostrar_menu_usuario()
            elif opcao == 'd':
                self.sistema.deslogar()
                self.mostrar_menu_inicial()
            elif opcao == '\\':
                print('nenhum menu acima deste')
            else:
                print('opção inválida')

    def mostrar_menu_conta(self):
        while True:
            opcao = input('\n\t\tconta:'
                          '\nd desativar'
                          '\n> ')

            if opcao == 'd':
                self.sistema.remover_conta()
            elif opcao == '\\':
                self.mostrar_menu_principal()
            else:
                print('opção inválida')

    def mostrar_menu_usuario(self):
        while True:
            opcao = input('\n\tusuarios:'
                          '\nl listar'
                          '\n> ')
            if opcao == 'l':
                self.sistema.listar_usuarios()
            elif opcao == '\\':
                self.mostrar_menu_principal()

    def mostrar_menu_inicial(self):

        while True:
            print(
                '\n\tBem-vindo ao Dez&Seis!'
                '\nl logar'
                '\nc cadastrar-se'
                '\ns sair')
            opcao = input('>')

            if opcao == 'l':
                self.mostrar_menu_login()
            elif opcao == 'c':
                self.mostrar_menu_cadastro()
            elif opcao == 's':
                exit()

    def mostrar_menu_login(self):
        email = input("Email: ")
        senha = input("Senha: ")

        try:
            self.sistema.autenticar(email, senha)
        except AuthenticationException:
            print('Email e senha não correspondem, tente novamente.')
