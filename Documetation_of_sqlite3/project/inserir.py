import sqlite3
from sqlite3 import Error
import os
os.system("clear")
caminho = os.getcwd()
print(caminho)

os.remove(caminho + "/projeto.db") if os.path.exists(caminho + "/projeto.db") else None

############ Criando uma conexão e um cursor ###################

try:
    con = sqlite3.connect(caminho + "/projeto.db")
    cur = con.cursor()
except Error as err:
    print(err)



# for comandos in tables:
#     cur.execute(comandos)

con.commit()
cur.close()
con.close()
print("ok")
