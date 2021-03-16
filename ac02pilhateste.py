'''
def empilhar(pilha, elemento):
    pilha.append(elemento)
    return pilha


pilha = [1, 2, 3, 4]
print(empilhar(pilha, 5))
'''

'''
def desempilhar(pilha):
    pilha.pop()
    return pilha


pilha = [1, 2, 3, 4]
print(desempilhar(pilha))
'''

'''
def topo(pilha):
    topo = pilha[-1]
    return topo


pilha = [1, 2, 3, 4]
print(topo(pilha))
'''

'''
def vazia(pilha):
    if pilha == []:
        return True
    else:
        return False


pilha = [1, 2]
print(vazia(pilha))
'''

'''
def tamanho(pilha):
    tamanho = len(pilha)
    return tamanho


pilha = [1, 2, 3, 4]
print(tamanho(pilha))
'''

'''
def pilha_letras(texto):
    pilha = []
    for x in texto:
        pilha.append(x)
    return pilha


texto = 'ola eu sou o guilherme'
print(pilha_letras(texto))
'''

'''
def menos_o_d(string):
    pilha = []
    for x in string:
        if x == 'd':
            if pilha != []:
                pilha.pop()
        else:
            pilha.append(x)
    return pilha


string = "abcddddxyzd"
print(menos_o_d(string))
'''

'''
def pilha_par_impar(pilha):
    auxiliar = []
    pilha_par = []
    pilha_impar = []
    tamanho = len(pilha)
    for x in range(tamanho):
        elemento = pilha.pop()
        auxiliar.append(elemento)
    for x in range(tamanho):
        desempilha = auxiliar.pop()
        if (desempilha % 2) == 0:
            pilha_par.append(desempilha)
        else:
            pilha_impar.append(desempilha) 
    
    return pilha_par, pilha_impar


pilha = [1, 3, 5]
print(pilha_par_impar(pilha))
'''