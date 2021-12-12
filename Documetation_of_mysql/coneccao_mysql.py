import mysql.connector
import os
os.system("clear")

config = {
            'user':'root',
            'password':'123456',
            'host':'localhost',
            'database':'ex001',
            'raise_on_warnings': True
        }

try:
    con = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    print(err)
else:
    db_info = con.get_server_info()
    print("Conectado ao servidor mysql versão: ", db_info)

cur = con.cursor()

if con.is_connected():
    cur.close()
    con.close()
    print("Conexão ao mysql foi encerrada!")
