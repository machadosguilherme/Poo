def posicoes_lista(lista, item):
    pos = 0
    newlist = []
    while item in lista:
        pos = lista.index(item)
        newlist.append(pos)
        lista[pos] = 0
    tupla = tuple(newlist)
    return tupla
