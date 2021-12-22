import os
from createTable import create
os.system("clear")
PATH = os.getcwd()

c = create("comercio")

sql_comandos = ["""create table if not exists produtos (
    id integer primary key autoincrement not null,
    date text,
    prod_name text,
    valor real
);"""]

for sql in sql_comandos:
    c.sql_create(sql)

