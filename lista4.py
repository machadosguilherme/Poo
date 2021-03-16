''' 
Escreva uma função chamada intercala_numeros que recebe como entrada duas listas de 
três elementos e retorna uma lista de seis elementos, com os números intercalados.

Exemplo: 
Suponha que as listas de entrada da função sejam: 
[1, 2, 3]
[4, 5, 6] 
Para estas listas, a função deve retornar:
[1, 4, 2, 5, 3, 6]
'''
def intercala_numeros(lista1,lista2):
    n=0
    for a in range(3):
        a=lista1[n]
        b=lista2[n]
        lista.append(a)
        lista.append(b)
        n+=1
    return lista
lista=[]
lista1=[]
for a in range (3):
    n= int(input('Digite: '))
    lista1.append(n)

lista2=[]
for a in range (3):
    n= int(input('Digite: '))
    lista2.append(n)

print(intercala_numeros(lista1, lista2))