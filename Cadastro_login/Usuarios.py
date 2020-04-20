from Banco import Banco
import sqlite3

class Usuarios(object):

    def __init__(self, idusuario = 0, nome = ' ',  celular = ' ', email = ' ', usuario = ' ', senha = ' '):
        self.info = {}
        self.idusuario = idusuario
        self.nome = nome
        self.celular = celular
        self.email = email
        self.usuario = usuario
        self.senha = senha

    def insertUser(self):

        banco = Banco()
        try:

            conn = banco.conexao.cursor()

            conn.execute("INSERT  into Usuarios (nome, celular, email, usuario, senha) values ('" + self.nome + "', '" + self.celular + "', '" + self.email + "', '" + self.usuario + "', '" + self.senha + "')")

            banco.conexao.commit()
            conn.close()

            return "Usuário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do usuário"

    def updateUser(self):

        banco = Banco()
        try:

            conn = banco.conexao.cursor()

            conn.execute("update Usuarios set nome = '" + self.nome + "', celular = '" + self.celular + "', email = '" + self.email + "', usuario = '" + self.usuario + "', senha = '" + self.senha + "', where idusuario = " + self.idusuario + " ")

            banco.conexao.commit()
            conn.close()

            return "Usuário atualizado com sucesso!"
        except:
            return "Ocorreu um erro na atualizão do usuário"

    def deleteUser(self):

        banco = Banco()
        try:

            conn = banco.conexao.cursor()
        
            conn.execute("delete from Usuarios where idusuario = " + self.idusuario + "")

            banco.conexao.commit()
            conn.close()

            return "Usuário excluido com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do usuário"

    def selectUser(self, idusuario):
        banco = Banco()
        try:

            conn = banco.conexao.cursor()
        
            conn.execute("select * from usuario where idususario = " + self.idusuario + "")

            for linha in  cursor:
                self.idusuario = linha[0]
                self.nome = linha[1]
                self.celular = linha[2]
                self.email = linha[3]
                self.usuario = linha[4]
                self.senha = linha[5]

            conn.close()

            return "Busca feita com sucesso!"
        except:
            return "Ocrreu um erro na busca do usuário"