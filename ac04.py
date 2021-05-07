# ALUNO 1: Guilherme da Silva Machado
# ALUNO 2: Thiago Barreto Amador
# ALUNO 3: Igor Higino de Oliveira


class Pessoa:
    def __init__(self, nome, rg, nascimento, telefone):
        self.nome = nome
        self.__rg = rg
        self.nascimento = nascimento
        self.telefone = telefone


class Instrutor(Pessoa):
    def __init__(self, nome, rg, nascimento, telefone, titulacao):
        super().__init__(nome, rg, nascimento, telefone)
        self.titulacao = titulacao
        self.turma = []

    def exibir(self):
        print(self.nome)
        print(self.nascimento)
        print(self.telefone)
        print(self.titulacao)
        print(self.turma)

    def turma_atribuida(self, turmas):
        self.turma.append(turmas)
        return self.turma


class Matricula:
    def __init__(self, matricula, dt_matricula, faltas):
        self.curso = Turma.tipo
        self.matricula = matricula
        self.dt_matricula
        self.faltas = faltas


class Turma:
    def __init__(
        self,
        numero_alunos,
        horario,
        tempo,
        dt_inicial,
        dt_final,
        tipo,
    ):
        self.numero_alunos = numero_alunos
        self.horario = horario
        self.tempo = tempo
        self.dt_inicial = dt_inicial
        self.dt_final = dt_final
        self.tipo = tipo
        self.alunos = []
        self.instrutor = []
        self.monitor = []

    def atribuir_alunos(self, nome):
        if (len(self.alunos) < self.numero_alunos):
            self.alunos.append(nome)
        else:
            print('Turma lotada')

    def atribuir_instrutor(self, nome):
        resul = ''
        if (len(self.instrutor) == 0):
            self.instrutor.append(nome)
            resul = nome
        else:
            print('Ja atribuido')
        return resul

    def atribuir_monitor(self, nome):
        resul = ''
        if (len(self.monitor) == 0):
            self.monitor.append(nome)
            resul = nome
        else:
            print('Ja atribuido')
        return resul

    def exibir(self):
        print(self.numero_alunos)
        print(self.horario)
        print(self.tempo)
        print(self.dt_inicial)
        print(self.dt_final)
        print(self.tipo)
        print(self.instrutor[0])
        print(self.monitor[0])


class Aluno(Pessoa, Matricula):
    def __init__(
        self,
        nome,
        rg,
        nascimento,
        telefone,
        matricula,
        dt_matricula,
        faltas,
        endereco,
        altura,
        peso
    ):
        Pessoa.__init__(nome, rg, nascimento, telefone)
        Matricula.__init__(matricula, dt_matricula, faltas)
        self.endereco = endereco
        self.altura = altura
        self.peso = peso

        def exibir(self):
            print(self.nome)
            print(self.nascimento)
            print(self.telefone)
            print(self.matricula)
            print(self.dt_matricula)
            print(self.faltas)
            print(self.endereco)
            print(self.altura)
            print(self.peso)


musculacao = Turma(10, 'As 13:00 e as 19:00', 'duração de 10 minutos',
                   '01/05/2021', '30/05/2021', 'Musculação')

zumba = Turma(40, 'As 15:00 e as 21:00', 'duração de 30 minutos',
              '01/05/2021', '30/05/2021', 'Zumba')

luta = Turma(25, 'As 12:00 e as 18:00', 'duração de 1:15 hora',
             '01/05/2021', '30/05/2021', 'Luta')

Instrutor1 = Instrutor('Carol', '32.123.45',
                       '03/03/1998', 1199999999, 'Professor')
Instrutor2 = Instrutor('Guilherme', '32.123.66',
                       '17/03/1998', 1199999999, 'Professor')
Instrutor3 = Instrutor('Gabriel', '32.123.01',
                       '10/04/1977', 1199999999, 'Professor')
Instrutor4 = Instrutor('Mario', '32.123.99',
                       '10/09/1974', 1199999999, 'Professor')

Instrutor1.turma_atribuida(musculacao.tipo)


natacao = Turma(
    30, 'As 14:00 e as 20:00', 'duração de 1 hora',
    '01/05/2021', '30/05/2021', 'Natação'
)
guilherme = Aluno('gui', 3298, '17/3/98', 119999999,
                  12345, '01/8/20', 5, 'Rua', 1.75, 80)

teste = natacao.atribuir_instrutor(Instrutor1.nome)

natacao.exibir()

teste2 = natacao.atribuir_instrutor(Instrutor2.nome)
print(teste2)

teste3 = natacao.atribuir_monitor(guilherme.nome)
print(teste3)
