#importando modulo do sql
import sqlite3

class Banco():
    
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()

    def createTable(self):
        conn = self.conexao.cursor()

        conn.execute("""CREATE TABLE if not exists  usuarios (
            idusuario integer primary key autoincrement,
            nome text, 
            celular text,
            email text,
            usuario text,
            senha text)""")

        self.conexao.commit()
        conn.close()