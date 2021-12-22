from conectado import conectado
import os

class create():
    def __init__(self, name) -> None:
        if os.path.exists(os.getcwd() + f"/{name}.db"):
            print("DATABASE EXISTS...")
        else:
            self. con = conectado()
            self.con.conectando(name)
    
    def sql_create(self, sql):
        self.cur = self.con.cursor()
        self.execute(sql)
        self.cur.close()
        self.con.fechandoBanco()
