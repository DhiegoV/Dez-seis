# -*- coding: utf-8 -*-

from src.ExceptFile3000 import AuthenticationException
from src.usuario import Usuario
from src.DAOs.SistemaDAO import SistemaDAO
from src.Interface.Menu import Menu

class Sistema:

    def __init__(self):
        self.menu = Menu(self)
        self.menu.mostrar_menu_inicial()
        self.usuario_logado = None

    def cadastrar_conta(self, usuario):
        SistemaDAO().cadastrar_conta(usuario)

    def remover_conta(self):
        SistemaDAO().remover_conta(self.usuario_logado)
        exit()

    def autenticar(self, email, senha):
        usuario = self.buscar_usuario(email)

        if usuario.get_senha() == senha:
            self.usuario_logado = usuario
            self.menu.mostrar_menu_principal()
        else:
            raise AuthenticationException

    def buscar_usuario(self, email):
        return SistemaDAO().buscar_usuario(email)

    def listar_usuarios(self):
        usuarios = SistemaDAO().obter_usuarios()
        self.menu.listar_usuarios(usuarios)

    def deslogar(self):
        self.usuario_logado = None

    def login(self):
        self.menu.mostrar_menu_login()
