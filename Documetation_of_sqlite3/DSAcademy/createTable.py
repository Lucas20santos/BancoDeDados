from conectado import conectado
import os

class create():
    def __init__(self, name) -> None:
        if os.path.exists(os.getcwd() + f"/{name}.db"):
            print("DATABASE EXISTS...")
        self.c = conectado()
        self.con = self.c.conectando(name)
    
    def sql_create(self, sql):
        self.cur = self.con.cursor()
        self.cur.execute(sql)
        self.cur.close()
        self.c.fechandoBanco()
