# Conecção do Python com MySQL

É preciso ter o mysql instalado no seu computador, caso 
você não tenha, siga as instruções vista nesse link:


[instalação mysql-server](http://www.bosontreinamentos.com.br/mysql/como-instalar-o-mysql-8-0-no-ubuntu-linux-18-04/)

## Intalando o conector do python com mysql usando o PIP

Abra o seu terminal e digite o comando

```pip install mysql-connector-python```

Agora é só esperar a instalação do pacote no seu python

## Criando uma conecção

- Primeiro vamos importar a biblioteca mysql.connector

```import mysql.connector` as cdb``

- Agora precisamos criar um objeto de conecção, dessa maneira:
```
try:
    con = cdb.connect(host='localhost', database='nome_do_banco', user='usuario', password='senha_usuario')
except:
    print("Connection Faleid")
```
