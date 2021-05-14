import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session


engine = sqlalchemy.create_engine('sqlite:///server05.db')
connection = engine.connect()

Base = declarative_base(engine)

session = Session()

connection.execute("""  CREATE TABLE IF NOT EXISTS PACIENTE(
                            ID INTEGER PRIMARY KEY,
                            NOME VARCHAR(255) NOT NULL,
                            CPF VARCHAR(14) NOT NULL,
                            IDADE INT NOT NULL)
""")
connection.execute("""  CREATE TABLE IF NOT EXISTS MEDICO(
                            ID INTEGER PRIMARY KEY,
                            NOME VARCHAR(255) NOT NULL,
                            CRM VARCHAR(14) NOT NULL,
                            ESPECIALIZACAO VARCHAR(255) NOT NULL)
""")

connection.execute("""  CREATE TABLE IF NOT EXISTS EXAME(
                            ID INTEGER PRIMARY KEY,
                            ID_MEDICO INT NOT NULL,
                            ID_PACIENTE INT NOT NULL,
                            DESCRICAO VARCHAR(255) NOT NULL,
                            RESULTADO VARCHAR(255) NOT NULL)
""")


class Paciente(Base):
    __tablename__ = 'PACIENTE'
    id = Column('ID', Integer, primary_key=True,
                autoincrement=True, nullable=False)
    nome = Column('NOME', String(255), nullable=False)
    cpf = Column('CPF', String(14), nullable=False)
    idade = Column('IDADE', Integer, nullable=False)

    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade


class Medico(Base):
    __tablename__ = 'MEDICO'
    id = Column('ID', Integer, primary_key=True,
                autoincrement=True, nullable=False)
    nome = Column('NOME', String(255), nullable=False)
    crm = Column('CRM', String(14), nullable=False)
    especializacao = Column('ESPECIALIZACAO', String(255), nullable=False)

    def __init__(self, nome, crm, especializacao):
        self.nome = nome
        self.crm = crm
        self.especializacao = especializacao


class Exame(Base):
    __tablename__ = 'EXAME'
    id = Column('ID', Integer, primary_key=True,
                autoincrement=True, nullable=False)
    id_medico = Column('ID_MEDICO', Integer, nullable=False)
    id_paciente = Column('ID_PACIENTE', Integer, nullable=False)
    descricao = Column('DESCRICAO', String(255), nullable=False)
    resultado = Column('RESULTADO', String(255), nullable=False)

    def __init__(self, id_medico, id_paciente, descricao, resultado):
        self.id_medico = id_medico
        self.id_paciente = id_paciente
        self.descricao = descricao
        self.resultado = resultado


medico1 = Medico('Caroline', '123.456.789-10', 'Neurocirurgiã')

paciente1 = Paciente('Guilherme s Machado', '406.181.611-80', 23)
paciente2 = Paciente('Marisa cordeiro', '635.331.611-34', 36)

session.add(medico1)
session.commit()

pacientes = [paciente1, paciente2]
session.add_all(pacientes)
session.commit()

exame1 = Exame(medico1.id,
               paciente1.id,
               'Sofre de alguma coisa que nenhum medico sabe',
               'Morre em breve'
               )
exame2 = Exame(medico1.id, paciente2.id,
               'Nao tenho mais criatividade', 'Esta bem')

exames = [exame1, exame2]
session.add_all(exames)
session.commit()

print('-' * 30)
teste1 = session.query(Medico).all()
for i in teste1:
    print(i.id, i.nome, i.crm, i.especializacao)

print('-' * 30)
teste2 = session.query(Paciente).all()
for i in teste2:
    print(i.id, i.nome, i.cpf, i.idade)

print('-' * 30)
teste3 = session.query(Exame).all()
for i in teste3:
    print(i.id, i.id_medico, i.id_paciente, i.descricao, i.resultado)
