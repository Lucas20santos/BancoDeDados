# Removendo o arquivo com o banco de daados SQLite (caso exista)
import os
os.system("clear")
os.remove("escola.db") if os.path.exists("escola.db") else None

import sqlite3
from sqlite3 import Error


# Criando uma conexão
try:
    con = sqlite3.connect("escola1.db")
except Error as err:
    print(err)
else:
    print("ok")

# criando um cursor
cur = con.cursor()

sql_create = """create table cursos(
    id integer primary key autoincrement,
    titulo varchar(100),
    categoria varchar(140)
);
"""

cur.execute(sql_create)

sql_insert = "insert into cursos values (?, ?, ?)"

recset = [(1000, 'ciencia de dados', 'Data Science'),
          (1001, 'Big Data Fundamentos','Big Data'),
          (1002, 'Python Fundamentos', 'Analise de Dados')
          ]

for rec in recset:
    cur.execute(sql_insert, rec)

con.commit()

sql_select = "select * from cursos"

cur.execute(sql_select)
dados = cur.fetchall()

for linha in dados:
    print(linha)


