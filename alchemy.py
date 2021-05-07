import sqlalchemy
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session


engine = sqlalchemy.create_engine('sqlite:///servidor.db')
connection = engine.connect()

Base = declarative_base(engine)

session = Session()

connection.execute(""" CREATE TABLE IF NOT EXISTS FUNCIONARIO (
                        ID INTEGER PRIMARY KEY,
                        NOME VARCHAR(255) NOT NULL,
                        IDADE INT NOT NULL,
                        SALARIO FLOAT NOT NULL)
                    """)


class Funcionario(Base):
    __tablename__ = 'FUNCIONARIO'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255))
    idade = Column('IDADE', Integer)
    salario = Column('SALARIO', Float)

    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario


funcionario1 = Funcionario('Guilherme', 23, 2500)
funcionario2 = Funcionario('Carol', 23, 3000)
funcionario3 = Funcionario('Mari', 44, 6000)

lista = [funcionario1, funcionario2, funcionario3]
session.add_all(lista)

print('-'*50)
resultado = session.query(Funcionario).all()
for i in resultado:
    print(i.id, i.nome, i.idade, i.salario)

print('-'*50)
teste = session.query(Funcionario).filter(Funcionario.salario > 1500).all()
for i in teste:
    print(i.id, i.nome, i.idade, i.salario)
