from src.usuario import Usuario
from src.ExceptFile3000 import *
from src.notificacao.PedidoAmizade import PedidoAmizade
import os

class Menu:

    def __init__(self, sistema):
        self.sistema = sistema

    def mostrar_menu_cadastro(self):
        self.limpar_tela()

        while True:
            nome = input("Nome: ")
            email = input("Email: ")
            senha = input("Senha: ")

            try:
                if nome == '':
                    raise NotNullAttributeNull
                if email == '':
                    raise NotNullAttributeNull
                if senha == '':
                    raise NotNullAttributeNull

                break
            except NotNullAttributeNull:
                print('Os atributos: nome, email ou senha não podem ser nulos')

        while True:
            try:
                idade = int(input("Idade: "))

                if idade < 0:
                    raise LessThanZeroAgeException
                break
            except ValueError:
                print('A idade só aceita numeros inteiros ou não nulos')
            except LessThanZeroAgeException:
                print('A idade não aceita numeros menores que 0')

        apelido = input("Apelido: ")

        usuario = Usuario(nome, email, idade, senha, '', apelido)


        self.sistema.cadastrar_usuario(usuario)

    def listar_usuarios(self, usuarios):
        saida = 'nomes:\n'
        for usuario in usuarios:
            saida += usuario[0] + '\n'

        self.print_limpo(saida)

    def mostrar_menu_principal(self):
        while True:
            self.limpar_tela()

            opcao = input('\n\tmenu principal:'
                          '\nC conta'
                          '\nU usuarios'
                          '\nn notificações'
                          '\nd deslogar'
                          '\n> ')
            if opcao == 'C':
                self.mostrar_menu_conta()
            elif opcao == 'n':
                self.mostrar_menu_notificacoes()
            elif opcao == 'U':
                self.mostrar_menu_usuario()
            elif opcao == 'd':
                self.sistema.deslogar()
                self.mostrar_menu_inicial()
            elif opcao == '\\':
                self.print_limpo('nenhum menu acima deste')
            else:
                self.print_limpo('opção inválida')

    def mostrar_menu_conta(self):
        while True:
            self.limpar_tela()
            opcao = input('\n\t\tconta:'
                          '\nd desativar'
                          '\n> ')

            if opcao == 'd':
                self.sistema.remover_usuario()
            elif opcao == '\\':
                self.mostrar_menu_principal()
            else:
                self.print_limpo('opção inválida')

    def mostrar_menu_notificacoes(self):
        notificacoes = self.sistema.buscar_notificacoes()
        if not notificacoes:
            self.print_limpo('Não há notificações')
            return
        while True:
            self.limpar_tela()
            for notificacao in notificacoes:
                print(notificacoes.index(notificacao), notificacao)
            opcao = input('número: ')

            if opcao == '\\':
                return
            try:
                notificacao = notificacoes[int(opcao)]
            except IndexError:
                self.print_limpo('opção inválida')

            if isinstance(notificacao, PedidoAmizade):
                self.mostrar_menu_pedido_amizade(notificacao)
            else:
                self.print_limpo(notificacao)

    def mostrar_menu_pedido_amizade(self, pedido_amizade):
        self.limpar_tela()
        while True:
            print(
                pedido_amizade,
                '\n'
                '\na aceitar'
                '\ni ignorar'
            )
            opcao = input('>')
            if opcao == 'a':
                self.sistema.estabelecer_amizade(pedido_amizade)
            elif opcao == 'i':
                return
            else:
                self.print_limpo('opcão inválida')

    def mostrar_menu_usuario(self):
        while True:
            self.limpar_tela()
            opcao = input('\n\tusuarios:'
                          '\nl listar'
                          '\na adicionar amigo'
                          '\n> ')
            if opcao == 'l':
                self.sistema.listar_usuarios()
            elif opcao == 'a':
                self.mostrar_menu_adicionar_amigo()
            elif opcao == '\\':
                self.mostrar_menu_principal()

    def mostrar_menu_adicionar_amigo(self):
        self.limpar_tela()
        email = input('Email do destinatário de sua solicitação: ')

        try:
            destinatario = self.sistema.buscar_usuario(email)
        except EmailNotFoundException:
            self.print_limpo('Email não encontrado :(')
            return

        self.sistema.enviar_pedido_amizade(destinatario)

    def mostrar_menu_inicial(self):
        while True:
            self.limpar_tela()
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
        self.limpar_tela()
        email = input("Email: ")
        senha = input("Senha: ")

        try:
            self.sistema.autenticar(email, senha)
        except AuthenticationException:
            self.print_limpo('Email e senha não correspondem, tente novamente.')
        except EmailNotFoundException:
            self.print_limpo('O email não foi encontrado :(')

    def print_limpo(self, mensagem):
        self.limpar_tela()
        print(mensagem)
        input('\n'
              'digite [Enter] para continuar')

    def limpar_tela(self):
        if os.name == 'posix' and os.system('env | grep TERM > /dev/null') == 0:
            # se num Linux, BSD, etc e se num terminal
            os.system('clear')
        elif os.name == 'nt':
            os.system('cls')
        else:
            print('\n' * 100)

