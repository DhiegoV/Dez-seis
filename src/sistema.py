# -*- coding: utf-8 -*-

from src.ExceptFile3000 import AuthenticationException
from src.usuario import Usuario
from src.DAOs.UsuarioDAO import UsuarioDAO
from src.Interface.Menu import Menu

class Sistema:

    def __init__(self):
        self.menu = Menu(self)
        self.usuariodao = UsuarioDAO()
        self.menu.mostrar_menu_inicial()
        self.usuario_logado = None

    def cadastrar_usuario(self, usuario):
        self.usuariodao.cadastrar_usuario(usuario)

    def remover_usuario(self):
        self.usuariodao.remover_usuario(self.usuario_logado)
        exit()

    def autenticar(self, email, senha):
        usuario = self.buscar_usuario(email)

        if usuario.get_senha() == senha:
            self.usuario_logado = usuario
            self.menu.mostrar_menu_principal()
        else:
            raise AuthenticationException

    def buscar_usuario(self, email):
        return self.usuariodao.buscar_usuario(email)

    def buscar_notificacoes(self):
        self.usuariodao.buscar_notificacoes(self.usuario_logado)

    def listar_usuarios(self):
        usuarios = self.usuariodao.obter_usuarios()
        self.menu.listar_usuarios(usuarios)

    def deslogar(self):
        self.usuario_logado = None

    def login(self):
        self.menu.mostrar_menu_login()

    def enviar_pedido_amizade(self, destinatario):
        pedido_amizade = \
            self.usuario_logado.get_nome() + ' quer ser seu amigo'
        self.usuariodao.enviar_notificacao(destinatario, pedido_amizade)
