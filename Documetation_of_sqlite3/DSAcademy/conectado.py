import sqlite3
from sqlite3 import Error

class conectado:
    def __init__(self) -> None:
        self.con = None
    
    def conectando(self, PATH_LOCAL: str):
        try:
            self.con = sqlite3.connect(PATH_LOCAL + "/escola.db")
        except Error as err:
            print(err)
        else:
            print("Conexão criada!")
    
    def fechandoBanco(self) -> None:
        self.con.close()
        print("Conexão Fechada!")

    

