def menores_notas(alunos):
    lista = []
    newdisc = {}
    for x in alunos:
        lista = alunos[x]
        menor = min(lista)
        newdisc[x] = menor
    return newdisc