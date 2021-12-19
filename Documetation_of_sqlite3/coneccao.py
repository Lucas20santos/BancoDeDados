import sqlite3
from sqlite3 import Error
import os
os.system("clear")

# Objetivo criar conexão e criar tabela

## Caminho do banco de dados
pathBanco = "/home/lucas/Documentos/Github/BancoDeDados/Documetation_of_sqlite3/banco.db"

## Criar uma conexão

def conexaoBanco():
    try:
        con = sqlite3.connect(pathBanco)
    except Error as err:
        print(err)
    return con

con = conexaoBanco()

## Comando para criar tabela

create_table = """create table teste(
    id integer primary key autoincrement,
    contato varchar(30),
    telefone varchar(14),
    email varchar(30)
);
"""

def criarTable(sql):
    try:
        cur = con.cursor()
        cur.execute(sql)
    except Error as err:
        print(err)
    else:
        print("Tabela Criada")

criarTable(create_table)
con.commit()
con.close()
