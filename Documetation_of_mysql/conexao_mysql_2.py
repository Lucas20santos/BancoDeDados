from mysql.connector import (connection)
import os
os.system("clear")

cnx = connection.MySQLConnection(user="root",
                                 password='123456',
                                 host="localhost",
                                 database="ex001")

if cnx.is_connected():
    print("Conectado")
    cnx.close()
