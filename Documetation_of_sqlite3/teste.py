sql_insert = "insert into cursos values (?, ?, ?)"

recset = [(1000, 'ciencia de dados', 'Data Science'),
          (1001, 'Big Data Fundamentos','Big Data'),
          (1002, 'Python Fundamentos', 'Analise de Dados')
          ]

for rec in recset:
    print(sql_insert, rec)
