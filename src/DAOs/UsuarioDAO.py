# -*- coding: utf-8 -*-

from src.usuario import Usuario
from src.ExceptFile3000 import *
from src.notificacao.PedidoAmizade import PedidoAmizade
from src.notificacao.Notificacao import Notificacao
import psycopg2

class UsuarioDAO:

    def __init__(self):
        self.conexao = psycopg2.connect(
            host="localhost",
            database="dez_seis",
            user="postgres",
            password="postgres")

    # ALTERAÇÕES

    def cadastrar_usuario(self, usuario):

        if usuario.get_nome() == '' \
                or usuario.get_email() == ''\
                or usuario.get_idade() == ''\
                or usuario.get_senha() == '':
            raise NotNullAttributeNull

        self.alterar_banco(
            'insert into usuario(nome, email, idade, senha, apelido) VALUES ' +
            '(\'{}\', \'{}\', \'{}\', \'{}\', \'{}\')'.format(
                usuario.get_nome(),
                usuario.get_email(),
                usuario.get_idade(),
                usuario.get_senha(),
                usuario.get_apelido()
            )
        )

    def enviar_notificacao(self, destinatario, mensagem):
        self.alterar_banco(
            'insert into notificacao(email_usuario, mensagem) values ' +
            '(\'{}\', \'{}\')'.format(destinatario.get_email(), mensagem)
        )

    def enviar_pedido_amizade(self, pedido_amizade):
        self.alterar_banco(
            'insert into notificacao(email_remetente, email_destinatario, mensagem, tipo) '
            "values ('{}', '{}', '{}', '{}')".format(
                pedido_amizade.get_remetente().get_email(),
                pedido_amizade.get_destinatario().get_email(),
                pedido_amizade.get_mensagem(),
                'PedidoAmizade'
            )
        )

    def estabelecer_amizade(self, remetente, destinatario):
        self.alterar_banco(
            'insert into amizade '
            "values ('{}', '{}')".format(
                remetente.get_email(),
                destinatario.get_email()
            )
        )

    def remover_usuario(self, usuario_logado):
        self.alterar_banco('delete from usuario where email=\'{}\''.format(usuario_logado.email))

    # CONSULTAS

    def buscar_usuario(self, email):
        lista_tuplas = self.consultar_banco('select * from usuario where email=\'{}\''.format(email))

        if not lista_tuplas:
            raise EmailNotFoundException

        tupla = lista_tuplas[0]

        usuario = Usuario(tupla[0], tupla[1], tupla[2], tupla[3], tupla[4], tupla[5])
        return usuario

    def obter_usuarios(self):
        usuarios = self.consultar_banco('select nome from usuario')
        return usuarios

    def buscar_notificacoes(self, usuario):
        tuplas = self.consultar_banco(
            'select * from notificacao where email_destinatario=\'{}\''
            .format(usuario.get_email())
        )

        if not tuplas:
            return

        notificacoes = []

        for tupla in tuplas:
            remetente = self.buscar_usuario(tupla[0])
            destinatario = self.buscar_usuario(tupla[1])
            mensagem = tupla[2]
            if tupla[3] == 'PedidoAmizade':
                notificacoes.append(PedidoAmizade(remetente, destinatario, mensagem))
            else:
                notificacoes.append(Notificacao(remetente, destinatario, mensagem))

        return notificacoes

    def criar_usuario(self, tupla):
        return Usuario(tupla[0], tupla[1], tupla[2], tupla[3], tupla[4], tupla[5])

    # MÉTODOS DE UTILIDADE

    def alterar_banco(self, comando_sql):
        cursor = self.conexao.cursor()
        cursor.execute(comando_sql)
        cursor.close()
        self.conexao.commit()

    def consultar_banco(self, comando_sql):
        cursor = self.conexao.cursor()
        cursor.execute(comando_sql)
        tupla = cursor.fetchall()
        cursor.close()
        return tupla
