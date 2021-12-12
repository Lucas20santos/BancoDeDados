create database cadastro
default character set utf8
default collate utf8_general_ci;

use cadastro;

-- drop table pessoas;

create table pessoas (
id int not null auto_increment,
nome varchar(30) not null,
nascimento date,
sexo enum('M', 'F'),
peso decimal(5, 2),
altura decimal(3,2),
nacionalidade varchar(20) default 'Brasil',
primary key (id)
) default charset = utf8;

insert into pessoas 
(id, nome, nascimento, sexo, peso, altura, nacionalidade)
values
(default, 'Lucas', '1992-02-21', 'M', '85', '1.65', 'Brasil');

insert into pessoas
(id, nome, nascimento, sexo, peso, altura, nacionalidade)
values
(default, 'Ana', '1994-03-11', 'F', '65', '1.65', 'Brasil'),
(default, 'Pedro', '1990-12-25', 'M', '80', '1.72', 'EUA'),
(default, 'Maria', '1999-05-30', 'F', '55', '1.55', 'Portugal'),
(default, 'Marcos', '1989-08-12', 'M', '100', '1.88', 'Espanha'),
(default, 'Joana', '2000-09-27', 'F', '70', '1.80', 'Brasil');


create table if not exists cursos(
idcurso int,
nome varchar (30) not null unique,
descricao text,
carga int unsigned,
totaulas int,
ano year default '2021',
primary key (idcurso)
)default charset = utf8;

-- drop table cursos; 

-- alter table cursos
-- add column idcurso int first;

-- alter table cursos
-- add primary key (idcursos);

insert into cursos values
('1', 'HTML4', 'Curso de HTML5', '40', '37', '2014'),
('2', 'Algoritmos', 'Lógica de Progamação', '20', '15', '2014'),
('3', 'Photoshop', 'Dicas de Photoshop CC', '10', '8', '2014'),
('4', 'PGP', 'Curso de PHP para iniciantes', '40', '20', '2010'),
('5', 'Jarva', 'Introdução à Linguagem Java', '10', '29', '2000'),
('6', 'MySQL', 'Banco de Dados MySQL', '30', '15', '2016'),
('7', 'Word', 'Curso completo de Word', '40', '30', '2016'),
('8', 'Sapateado', 'Danças Rítmicas', '40', '37', '2018'),
('9', 'Cozinha Árabe', 'Aprender a fazer Kibe', '40', '30', '2018'),
('10', 'YouTuber', 'Gerar polêmica e ganhar inscritos', '5', '2', '2018');

select * from pessoas;
select * from cursos;

-- Filtragem da tabela por colunas
 
select * from cursos
order by nome;

select * from cursos
order by nome desc;

select nome, carga, ano from cursos
order by nome;

-- Filtragem da tabela por linhas usando o where
select * from cursos
where ano = '2016'
order by nome;

select nome, carga from cursos
where ano <= '2015'
order by nome;

select nome, ano from cursos
where ano between 2014 and 2016
order by ano, nome;

select nome, ano from cursos
where ano in (2014, 2016)
order by ano;

select * from cursos
where carga > 35 and totaulas < 40;
