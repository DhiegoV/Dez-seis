
import psycopg2

class SistemaDAO:

    def __init__(self):
        self.conexao = psycopg2.connect(
            host="localhost",
            database="dez_seis",
            user="postgres",
            password="postgres")

    def cadastrar_conta(self, nome, email, senha, idade, apelido):
        cursor = self.conexao.cursor()
        cursor.execute(
            'insert into usuario(nome, email, idade, senha, apelido) VALUES ' +
            '(\'{}\', \'{}\', \'{}\', \'{}\', \'{}\')'.format(nome, email, idade, senha, apelido)
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

        usuario = dict(
            nome=tupla[0],
            email=tupla[1],
            idade=tupla[2],
            senha=tupla[3],
            status=tupla[4],
            apelido=tupla[5]
        )
        return usuario
