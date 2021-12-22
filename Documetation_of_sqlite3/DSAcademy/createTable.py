from conectado import conectado
import os

class create():
    def __init__(self, DATABASENAME) -> None:
        if os.path.exists(os.getcwd() + DATABASENAME + ".db"):
            print("DATABASE EXISTS...")
        else:
            self. con = conectado()
            self.con.conectando(os.getcwd() + f"/{DATABASENAME}" + ".db")
    
    def sql_create(self, sql):
        self.cur = self.con.cursor()
        self.execute(sql)
        self.cur.close()
