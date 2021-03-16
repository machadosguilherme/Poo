def posicao(lista, indice):
    pos = lista[indice]
    print(' O nome nesse posiçao é: ', pos)


lista = []
for a in range(5):
    n = input('Digite um nome')
    lista.append(n)

b = int(input('Digite uma posiçao: '))
posicao(lista, b)