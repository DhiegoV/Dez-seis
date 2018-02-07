from src.usuario import Usuario
from src.ExceptFile3000 import EmailNotFoundException, NotNullAttributeNull
import psycopg2

class SistemaDAO:

    def __init__(self):
        self.conexao = psycopg2.connect(
            host="localhost",
            database="dez_seis",
            user="postgres",
            password="postgres")

    def cadastrar_conta(self, usuario):

        if usuario.get_nome() == '' \
                or usuario.get_email() == ''\
                or usuario.get_idade() == ''\
                or usuario.get_senha() == '':
            raise NotNullAttributeNull

        cursor = self.conexao.cursor()
        cursor.execute(
            'insert into usuario(nome, email, idade, senha, apelido) VALUES ' +
            '(\'{}\', \'{}\', \'{}\', \'{}\', \'{}\')'.format(
                usuario.get_nome(),
                usuario.get_email(),
                usuario.get_idade(),
                usuario.get_senha(),
                usuario.get_apelido()
            )
        )
        cursor.close()
        self.conexao.commit()

    def remover_conta(self, usuario_logado):
        cursor = self.conexao.cursor()
        cursor.execute('delete from usuario where email=\'{}\''.format(usuario_logado.email))
        cursor.close()
        self.conexao.commit()

    def obter_usuarios(self):
        cursor = self.conexao.cursor()
        cursor.execute('select nome from usuario')
        usuarios = cursor.fetchall()
        cursor.close()
        return usuarios

    def buscar_usuario(self, email):
        cursor = self.conexao.cursor()
        cursor.execute('select * from usuario where email=\'{}\''.format(email))
        tupla = cursor.fetchone()
        cursor.close()

        if not tupla:
            raise EmailNotFoundException

        usuario = Usuario(tupla[0], tupla[1], tupla[2], tupla[3], tupla[4], tupla[5])
        return usuario
