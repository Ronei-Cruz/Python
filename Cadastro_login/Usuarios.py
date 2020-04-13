from Banco import Banco

class Usuarios(object):

    def __init__(self, idusuario = 0, nome = '',  celular = '', email = '', usuario = '', senha = ''):
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

            c = banco.conexao.cursor()

            c.execute("isnsert  into ususario (nome, celular, email, usuario, senha) values ('" + self.nome + "', '" + self.celular + "', '" + self.email + "', '" + self.usuariio + "', '" + self.senha + "')")

            banco.conexao.commit()
            c.clese()

            return "Usuário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na isnserção do usuário"

    def updateUser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("update usuario set nome = '" + self.nome + "', '" + self.celular + "', '" + self.email + "', '" + self.usuario + "', '" + self.senha + "' "'where idusuario = " + self.idusuario + "')

            banco.conexao.commit()
            c.close()

            return "Usuário atualizado com sucesso!"
        except:
            return "Ocorreu um erro na atualizão do usuário"

    def deleteUser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()
        
            c.execute("delete from usuario where idusuario = " + self.idusuario + "")

            banco.conexao.commit()
            c.close()

            return "Usuário excluido co sucesso!"
        except:
            return "Ocorreu um erro na exclusão do usuário"

    def selectUser(self, idusuario):
        banco = Banco()
        try:

            c = banco.conexao.cursor()
        
            c.execute("select * from usuario where idususario = " + idusuario + "")

            for linha in  c:
                self.idusuario = linha[0]
                self.nome = linha[1]
                self.celular = linha[2]
                self.email = linha[3]
                self.usuario = linha[4]
                self.senha = linha[5]

            c.close()

            return "Busca feita com sucesso!"
        except:
            return "Ocrreu um erro na busca do usuário"