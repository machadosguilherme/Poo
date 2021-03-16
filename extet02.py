def funcao_1():
    print('Inicio da funçao')
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(15):
        print(lista[i])
    print('fim da funçao')


try:
    print('Inicio do programa')
    funcao_1()
    print('Fim do programa')

except IndexError:
    print('Oooops, o indice solicitado é maior que o indice existente.')
finally:
    print('Programa executado com sucesso.')