# PROGRAMAÇÃO ORIENTADA A OBJETOS
# ATIVIDADE CONTÍNUA 03

# INSIRA ABAIXO O NOME DOS ALUNOS DO GRUPO
# ALUNO 1: Guilherme da silva Machado
# ALUNO 2: Thiago Barreto Amador
# ALUNO 3: Igor Higino de Oliveira
# ALUNO 4: nome
# ALUNO 5: nome
# ALUNO 6: nome


class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.casas = []

    def incluir_casa(self, casa):
        self.casas.append(casa)


class Casa:
    def __init__(self, nome, animal):
        self.nome = nome
        self.animal = animal
        self.diretor = None
        self.monitor = None

    def set_diretor(self, professor):
        self.diretor = professor

    def set_monitor(self, aluno):
        self.monitor = aluno


class Professor:
    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento
        self.disciplinas = []

    def incluir_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)


class Aluno:
    def __init__(self, nome, nascimento, tipo):
        self.nome = nome
        self.nascimento = nascimento
        self.tipo = tipo
        self.casa = None
        self.__triunfos = 0
        self.__mau_feitos = 0

    def set_casa(self, casa):
        self.casa = casa

    def incluir_triunfo(self, triunfos):
        self.__triunfos += triunfos

    def incluir_mau_feito(self, mau_feito):
        self.__mau_feitos += mau_feito

    def get_triunfos(self):
        return self.__triunfos

    def get_mau_feitos(self):
        return self.__mau_feitos


class Disciplina:
    def __init__(self, nome, ementa):
        self.nome = nome
        self.ementa = ementa
        self.alunos = []

    def incluir_aluno(self, aluno):
        self.alunos.append(aluno)
