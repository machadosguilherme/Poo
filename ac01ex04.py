def reprovados(alunos):
    media = 0
    lista = []
    for x in alunos:
        aluno = x
        cont = 0
        notas = alunos[x]
        cont = len(notas)
        resul = sum(notas)
        media = resul / cont
        if media < 6:
            lista.append(aluno)
    return lista