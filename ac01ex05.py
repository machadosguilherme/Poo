def incluir_nota(alunos,nome,nota):
    if nome in alunos:
        lista = []
        lista = alunos[nome] 
        lista.append(nota)
    return alunos