# ATIVIDADE CONTÍNUA 05

# NOMES DOS ALUNOS: (MÁXIMO 6):
# ALUNO 1: Guilherme da Silva Machado
# ALUNO 2: Igor Higino
# ALUNO 3: Thiago Barreto
# ALUNO 4: nome
# ALUNO 5: nome
# ALUNO 6: nome


import sqlalchemy

from sqlalchemy import Column, Integer, String, Float, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

# Criar Conexão com Banco SQLITE
engine = sqlalchemy.create_engine("sqlite:///server.db")
connection = engine.connect()
Base = declarative_base(engine)
session = Session()


class Filme(Base):

    # FAZER O MAPEAMENTO DA TABELA
    __tablename__ = "FILME"
    id = Column("ID", Integer, autoincrement=True, primary_key=True)
    titulo = Column("TITULO", String(255), nullable=False)
    ano = Column("ANO", Integer, nullable=False)
    genero = Column("GENERO", String(255), nullable=False)
    duracao = Column("DURACAO", Integer, nullable=False)
    pais = Column("PAIS", String(255), nullable=False)
    diretor = Column("DIRETOR", String(255), nullable=False)
    elenco = Column("ELENCO", String(255), nullable=False)
    avaliacao = Column("AVALIACAO", Float, nullable=False)
    votos = Column("VOTOS", Integer, nullable=False)

    # Método construtor

    def __init__(
            self,
            titulo,
            ano,
            genero,
            duracao,
            pais,
            diretor,
            elenco,
            avaliacao,
            votos):
        self.titulo = titulo
        self.ano = ano
        self.genero = genero
        self.duracao = duracao
        self.pais = pais
        self.diretor = diretor
        self.elenco = elenco
        self.avaliacao = avaliacao
        self.votos = votos


# Classe para interação com o Banco de Dados
class BancoDeDados:
    def criar_tabela(self):
        # Cria a tabela FILME no banco de dados
        connection.execute("""CREATE TABLE IF NOT EXISTS FILME(
                              ID INTEGER PRIMARY KEY,
                              TITULO VARCHAR(255) NOT NULL,
                              ANO INT NOT NULL,
                              GENERO VARCHAR(255) NOT NULL,
                              DURACAO INT NOT NULL,
                              PAIS VARCHAR(255) NOT NULL,
                              DIRETOR VARCHAR(255) NOT NULL,
                              ELENCO VARCHAR(255) NOT NULL,
                              AVALIACAO FLOAT NOT NULL,
                              VOTOS INT NOT NULL)""")

    def incluir(self, filme):
        '''
        Recebe um objeto Filme e armazena esse
        objeto no banco de dados.
        '''
        session.add(filme)
        session.commit()

    def incluir_lista(self, filmes):
        '''
        Recebe uma lista de objetos Filme e armazena esses
        objetos no banco de dados
        '''
        session.add_all(filmes)
        session.commit()

    def alterar_avaliacao(self, filme, avaliacao):
        '''
        Recebe um objeto filme e altera sua avaliação de
        acordo com o valor do parametro avaliacao
        '''
        
        return

    def excluir(self, id):
        '''
        Recebe o id de um filme e exclui o filme correspondente
        do banco de dados
        '''
        pass

    def buscar_todos(self):
        '''
        Realiza busca no banco de dados e retorna uma
        lista de objetos Filme com todos os registros,
        ordenados de forma crescente pelo titulo.
        '''
        lista = []
        resultado = session.query(Filme).order_by(Filme.titulo)
        for x in resultado:
            lista.append(x)
        return lista

    def buscar_por_id(self, id):
        '''
        Realiza busca no banco de dados e retorna um
        objeto Filme de acordo com o seu id
        '''
        filme = ''
        resultado2 = session.query(Filme).filter(Filme.id == id)
        for x in resultado2:
            filme = x.id,
            x.titulo,
            x.ano,
            x.genero,
            x.duracao,
            x.pais,
            x.diretor,
            x.elenco,
            x.avaliacao,
            x.votos
        return filme

    def buscar_por_ano(self, ano):
        '''
        Realiza busca no banco de dados e retorna uma
        lista de objetos Filme de um ano específico,
        ordenado pelo ID de forma crescente
        '''
        lista1 = []
        resultado3 = session.query(Filme).filter(
            Filme.ano == ano
            ).order_by(Filme.id)
        for x in resultado3:
            lista1.append(x)
        return lista1

    def buscar_por_genero(self, genero):
        '''
        Realiza busca no banco de dados e retorna uma
        lista de objetos Filme de um gênero específico,
        ordenados pelo titulo de forma crescente
        '''
        lista = []
        resultado = session.query(Filme).filter(Filme.genero == genero).order_by(Filme.titulo)
        for x in resultado:
            lista.append(x)
        return lista

    def buscar_por_elenco(self, ator):
        '''
        Realiza busca no banco de dados e retorna uma
        lista de objetos Filme que tenha um determinado ator/atriz como parte
        do elenco, ordenados pelo ano de lançamento em ordem crescente
        '''
        lista3 = []
        resultado5 = session.query(Filme).filter(ator.in_(session.query(Filme.elenco)).order_by(Filme.ano))
        for x in resultado5:
            lista3.append(x)
        return lista3

    def buscar_melhores_do_ano(self, ano):
        '''
        Realiza busca no banco de dados e retorna uma lista de
        objetos Filme de um ano específico, com avaliação
        maior ou igual a 90
        Deve retornar ordenado pela avaliação de forma decrescente.
        DICA - utilize a função:
            .order_by(desc(Filme.avaliacao))
        '''
        lista4 = []
        resultado6 = session.query(Filme).filter(
            Filme.ano == ano, Filme.avaliacao >= 90.00
            ).order_by(desc(Filme.avaliacao))
        for x in resultado6:
            lista4.append(x)
        return lista4

    def exportar_filmes(self, nome_arquivo):
        '''
        Exporta os dados contidos na tabela de filmes para um arquivo de texto
        O arquivo deve conter uma listagem dos filmes, ordenados pelos titulos
        dos filmes, contendo os dados de cada filme em uma linha, no formato:
        titulo;year;genero;duracao;país;diretor;elenco;avaliacao;votos
        '''
        arquivo = open('filmessaida.txt', 'w', encoding='UTF-8')
        resultado7 = session.query(Filme).order_by(Filme.titulo)
        for x in resultado7:
            arquivo.write(
                x.titulo + ';' +
                str(x.ano) + ';' +
                x.genero + ';' +
                str(x.duracao) + ';' +
                x.pais + ';' +
                x.diretor + ';' +
                x.elenco + ';' +
                str(x.avaliacao) + ';' +
                str(x.votos) + ';' '\n')
        return

    def importar_filmes(self, nome_arquivo):
        '''
        Recebe como parâmetro o nome de um arquivo de texto e importa os
        dados contidos no arquivo para o banco de dados.
        Considere que o arquivo contém uma listagem de filmes no formato:
        titulo;year;genero;duracao;país;diretor;elenco;avaliacao;votos
        '''
        arquivo2 = open(nome_arquivo, 'r', encoding='UTF-8')
        filmes1 = []
        for line in arquivo2:
            lista = line.split(';')
            filmes = Filme(
                    lista[0],
                    int(lista[1]),
                    lista[2],
                    int(lista[3]),
                    lista[4],
                    lista[5],
                    lista[6],
                    float(lista[7]),
                    int(lista[8])
                    )
            filmes1.append(filmes)
        session.add_all(filmes1)
        return filmes

# EXEMPLO DE PROGRAMA PRINCIPAL


banco = BancoDeDados()
banco.criar_tabela()
banco.importar_filmes('movies.txt')

filme = Filme('Veloses', 00, 'acao', 96, 'USA', 'Eu', '(Gui, carol, eu, nois)', 95, 250)
filme2 = Filme('Crepuscilo', 11, 'drama', 56, 'USA', 'naosei', '(edward, bella)', 00, 300)

teste = [filme, filme2]

'''banco.incluir(filme)'''
banco.incluir_lista(teste)

'''# Busca todos os filmes
lista = banco.buscar_todos()
print('-'*60)
for f in lista:         # exibe lista de filmes
    print(f.id,
    f.titulo,
    f.ano,
    f.genero,
    f.duracao,
    f.pais,
    f.diretor,
    f.elenco,
    f.avaliacao,
    f.votos)
'''
'''# Busca por ano
lista = banco.buscar_por_ano(2019)
print('-'*60)
for f in lista:         # exibe lista de filmes
    print(f.id,
    f.titulo,
    f.ano,
    f.genero,
    f.duracao,
    f.pais,
    f.diretor,
    f.elenco,
    f.avaliacao,
    f.votos)'''

'''# Busca por genero
lista = banco.buscar_por_genero('Crime')
print('-'*60)
for f in lista:         # exibe lista de filmes
    print(f.id, f.titulo, f.ano, f.genero)
'''
'''# Busca por elenco
lista = banco.buscar_por_elenco('Nicole')
print('-'*60)
for f in lista:         # exibe lista de filmes
    print(f.id,
    f.titulo,
    f.ano,
    f.genero,
    f.duracao,
    f.pais,
    f.diretor,
    f.elenco,
    f.avaliacao,
    f.votos)'''

'''# Busca melhores do ano ################################################# resolvido
lista = banco.buscar_melhores_do_ano('2019')
print('-'*60)
for f in lista:         # exibe lista de filmes
    print(f.id,
    f.titulo,
    f.ano,
    f.genero,
    f.duracao,
    f.pais,
    f.diretor,
    f.elenco,
    f.avaliacao,
    f.votos)'''


banco.exportar_filmes('saida.txt')
