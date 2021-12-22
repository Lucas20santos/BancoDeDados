import sqlite3
from sqlite3 import Error
import os
os.system("clear")
caminho = os.getcwd()

os.remove(caminho + "/projeto.db") if os.path.exists(caminho + "/projeto.db") else None

############ Criando uma conexão e um cursor ###################

try:
    con = sqlite3.connect(caminho + "/projeto.db")
    cur = con.cursor()
except Error as err:
    print(err)

tables = ["""create table dono(
        id integer primary key autoincrement,
        nome varchar(45),
        sexo varchar(10),
        email varchar(30),
        telefone varchar(15)
    );""",
    """create table animal(
        id integer primary key autoincrement,
        nome varchar(30),
        castrado varchar(3),
        especie varchar(30),
        data_nascimento date,
        peso decimal(5, 2)
    );""",
    """create table cachorro(
        id integer primary key autoincrement,
        raca varchar(30)
    );""",
    """create table gato(
        id integer primary key autoincrement,
        raca varchar(30)
    );""",
    """create table racao(
        id integer primary key autoincrement,
        nome varchar(40),
        slot integer,
        quantidade integer
    );"""
]

for comandos in tables:
    cur.execute(comandos)

cachorros = [ (1, 'vira-lata'), (2, 'shih tzu'), (3 , 'Yorkshire Terrier'),
(4, 'Poodle') ,(5, 'Lhasa Apso'),(6, 'Buldogue Francês'),
(7, 'Pinscher'),(8, 'Golden Retriever'),(9, 'Spitz Alemão','Maltês')]

gatos = [(1,'Vira-lata'),(2,'Siamês'),(3,'Maine Coon'),(4,'Angorá'),
(5,'Sphynx'),(6 ,'Ragdoll'),(7 ,'Ashera'),(8 ,'American Shorthair'),
(9 ,'Exótico'),(10,'Persa')]

racoes_gatos_castrado = [(1, 'Ração Royal Canin Sterilised'), (2, 'Ração PremieR Ambientes Internos')]

racoes_cachorros_castrado = [(1, 'Ração Farmina Cibau Light'), (2, 'Ração PremieR Ambientes Internos')]

racoes_cachorro = [(1, 'Golden Formula Frango e Arroz'), (2, 'Naturalis Frango, Peru e Frutas')]

racoes_gatos = [(1,'GranPlus Adultos'), (2, 'Whiskas Adultos')]

# Gatos
sql_insert_gatos = "insert into gato values (?, ?)"
for rgc in gatos:
    cur.execute(sql_insert_gatos, rgc)

# Cachorros
sql_insert_cachorros = "insert into cachorro values (?, ?)"

for rgc in gatos:
    cur.execute(sql_insert_cachorros, rgc)

sql_select = "select * from gato"
cur.execute(sql_select)
dados = cur.fetchall()

print("======================TABELA GATOS========================")
for k, v in enumerate(dados):
    print(f" {k + 1} - {v[1]}")
print("==========================================================")

con.commit()
cur.close()
con.close()
