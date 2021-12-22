import sqlite3
from sqlite3 import Error
import os

PATH = os.getcwd()

class conectado:
    def __init__(self) -> None:
        self.con = None
    
    def conectando(self, name):
        try:
            self.con = sqlite3.connect(PATH + f"/{name}.db")
        except Error as err:
            print("Erro: ", err)
        else:
            print("Conexão criada!")
    
    def fechandoBanco(self) -> None:
        self.con.close()
        print("Conexão Fechada!")

    

