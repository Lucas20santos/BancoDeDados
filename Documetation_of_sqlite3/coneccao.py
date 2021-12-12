import sqlite3
import os

# Quando é baixado o anaconda, ele instala o sqlite3

PATH = "/home/lucas/Documentos/Github/BancoDeDados/escola.db"

# Essa funçao verifica se existe um banco 
# de dados no caminho especificado
# na variável PATH. 
# Caso esse banco exista, ele será apagado.
def existeBanco(PATH):
    os.remove(PATH) if os.path.exists(PATH) else None


# Criando uma conexão chamada con
# Passando o caminho aonde o banco de dados vai ser criado
# esse caminho pode ser colocado em qualquer lugar
def coneccao(PATH):
    con = sqlite3.connect(PATH)
    return con

# 
def fecharConeccao(con):
    con.close()


# Criando um cursor para percorrer todos os registro do banco de dados
def cursorBanco(con):
    return con.cursor()

# criando uma instancia da classe conecção do sqlite3 
con1 = coneccao(PATH)

# criando uma instancia da classe cursor, para 
# fazer as consultas no banco de dados
cur = cursorBanco(con1)

sql_create = f'create table cursos '\
        '(id integer primary dey, '\
        'titulo varchar(100) '\
        'categoria varchar(140))'

cur.execute(sql_create)
