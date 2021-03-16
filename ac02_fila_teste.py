
def enfileirar(fila, elemento):
    fila.append(elemento)
    return fila

'''
fila = [1, 2, 3, 4]
elemento = 5
print(enfileirar(fila, elemento))
'''


def desenfileirar(fila):
    newfila = fila.pop(0)
    return newfila

'''
fila = [1, 2, 3, 4]
print(desenfileirar(fila))
'''


'''
def primeiro(fila):
    primeiro = fila[0]
    return primeiro


fila = [1, 2, 3, 4]
print(primeiro(fila))'''


'''
def vazia(fila):
    if fila == []:
        return True
    else:
        return False


fila = []
print(vazia(fila))'''


'''
def tamanho(fila):
    tamanho = len(fila)
    return tamanho


fila = [1, 2, 3, 4]
print(tamanho(fila))'''


def vira_n(fila, n):
    primeiro = fila[0]
    while primeiro != n:
        primeiro = fila[0]
        desenfileirar(fila)
        fila = enfileirar(fila, primeiro)
    return fila


fila = [3, 4, 5]
print(vira_n(fila, 5))

'''
def vira_4_mata_1(fila):
    for x in range(4):
        primeiro = fila[0]
        desenfileirar(fila)
        enfileirar(fila, primeiro)
    fila.pop(0)
    return fila


fila = [1, 2, 3, 4, 5]
print(vira_4_mata_1(fila))
'''
'''

def inverte(fila):
    pilha = []
    tamanho = len(fila)
    cont = 0
    while cont < tamanho:
        elemento = desenfileirar(fila)
        pilha.append(elemento)
        cont += 1
    while cont > 0:
        voltando = pilha.pop()
        enfileirar(fila, voltando)
        cont -= 1
    return fila


fila = [1, 2, 3, 4]
print(inverte(fila))
'''