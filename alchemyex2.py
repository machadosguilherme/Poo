import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session


engine = sqlalchemy.create_engine('sqlite:///servidor.db')
connection = engine.connect()

Base = declarative_base(engine)

session = Session()

connection.execute("""  CREATE TABLE IF NOT EXISTS AUTOR(
                            ID INTEGER PRIMARY KEY,
                            NOME VARCHAR(255) NOT NULL)
                    """)
connection.execute("""  CREATE TABLE IF NOT EXISTS LIVRO(
                            ID INTEGER PRIMARY KEY,
                            TITULO VARCHAR(255) NOT NULL,
                            PAGINAS INT NOT NULL,
                            AUTOR_ID INT NOT NULL)
""")


class Autor(Base):
    __tablename__ = 'AUTOR'
    id = Column('ID', Integer, primary_key=True,
                autoincrement=True)
    nome = Column('NOME', String(255), nullable=False)

    def __init__(self, nome):
        self.nome = nome


class Livro(Base):
    __tablename__ = 'livro'
    id = Column('ID', Integer, primary_key=True,
                autoincrement=True, nullable=False)
    titulo = Column('TITULO', String(255), nullable=False)
    paginas = Column('PAGINAS', Integer, nullable=False)
    autor_id = Column('AUTOR_ID', Integer, nullable=False)

    def __init__(self, titulo, paginas, autor_id):
        self.titulo = titulo
        self.paginas = paginas
        self.autor_id = autor_id


autor1 = Autor('Guilherme')
autor2 = Autor('Caroline')

lista1 = [autor1, autor2]
session.add_all(lista1)
session.commit()

print('='*50)
resultado = session.query(Autor).order_by(Autor.nome)
for i in resultado:
    print(i.id, i.nome)


livro1 = Livro('Python para iniciantes', 450, autor1.id)
livro2 = Livro('Tecnicas de invasão', 300, autor2.id)


lista2 = [livro1, livro2]

session.add_all(lista2)
session.commit()

print('='*50)
teste = session.query(Livro).order_by(Livro.titulo)
for i in teste:
    print(i.titulo, i.paginas, i.autor_id)
