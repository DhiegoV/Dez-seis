from src.usuario import Usuario
from src.ExceptFile3000 import EmailNotFoundException, NotNullAttributeNull
from datetime import datetime
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

    def remover_usuario(self, usuario_logado):
        self.alterar_banco('delete from usuario where email=\'{}\''.format(usuario_logado.email))

    # CONSULTAS

    def buscar_usuario(self, email):
        tupla = self.consultar_banco('select * from usuario where email=\'{}\''.format(email))

        if not tupla:
            raise EmailNotFoundException

        usuario = Usuario(tupla[0], tupla[1], tupla[2], tupla[3], tupla[4], tupla[5])
        return usuario

    def obter_usuarios(self):
        usuarios = self.consultar_banco('select nome from usuario')
        return usuarios

    # MÉTODOS DE UTILIDADE

    def alterar_banco(self, comando_sql):
        cursor = self.conexao.cursor()
        cursor.execute(comando_sql)
        cursor.close()
        self.conexao.commit()

    def consultar_banco(self, comando_sql):
        cursor = self.conexao.cursor()
        tupla = cursor.execute(comando_sql)
        cursor.close()
        return tupla
