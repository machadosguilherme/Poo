# INSIRA ABAIXO OS NOMES DOS ALUNOS DO GRUPO (máximo 5 alunos)
# ALUNO 1: Guilherme da Silva Machado
# ALUNO 2: Thiago Barreto Amador 
# ALUNO 3: Igor Higino de Oliveira
# ALUNO 4:
# ALUNO 5:


'''
Escreva uma função com o nome pertence, que recebe como argumentos de
entrada uma tupla e dois itens e retorna True, se os dois itens estiverem
armazenado na tupla, e False, caso contrário.
'''


def pertence(tupla, item1, item2):
    if item1 in tupla:
        if item2 in tupla:
            return True
        else:
            return False
    else:
        return False
    return


'''
Escreva uma função chamada substituir que recebe como argumentos de entrada uma
lista e dois itens (velho e novo) e retorna uma lista onde todas as ocorrências
do item velho são substituídas pelo item novo.
'''


def substituir(lista, velho, novo):
    while velho in lista:
        pos = lista.index(velho)
        lista[pos] = novo
    return lista


'''
Escreva uma função chamada posicoes_lista que recebe como argumentos de
entrada uma lista e um item, e retorna uma tupla contendo todas os índices
em que o item aparece na lista.
'''


def posicoes_lista(lista, item):
    newlist = []
    while item in lista:
        pos = lista.index(item)
        newlist.append(pos)
        lista[pos] = 0
    tupla = tuple(newlist)
    return tupla


'''
Suponha um dicionário onde a chave é o nome de um aluno e o valor uma lista
de notas. Escreva uma função chamada reprovados que recebe como argumento de
entrada o dicionário e retorna uma lista com o nome dos alunos reprovados
(um aluno é reprovado quando a média das suas notas é inferior a 6).
'''


def reprovados(alunos):
    lista = []
    for x in alunos:
        notas = alunos[x]
        cont = len(notas)
        soma = sum(notas)
        media = soma / cont
        if media < 6:
            lista.append(x)
            
    return lista


'''
Suponha um dicionário onde a chave é o nome de um aluno e o valor uma lista de
notas. Escreva uma função chamada incluir_nota que recebe como argumentos de
entrada o dicionário, o nome de um aluno e uma nota. A função deve inserir a
nota na lista de notas do aluno correspondente e retornar o dicionário com as
alterações realizadas.
'''


def incluir_nota(alunos, nome, nota):
    if nome in alunos:
        lista = []
        lista = alunos[nome] 
        lista.append(nota)
    return alunos


'''
Suponha um dicionário onde a chave é o nome de um aluno e o valor uma lista
de notas. Escreva uma função chamada menores_notas que recebe como
argumentos de entrada o dicionário e retorna outro dicionário com a
menor nota de cada aluno.
'''


def menores_notas(alunos):
    lista = []
    newdisc = {}
    for x in alunos:
        lista = alunos[x]
        menor = min(lista)
        newdisc[x] = menor
    return newdisc