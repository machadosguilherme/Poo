''' Preencha duas tuplas com 5 números cada, informados pelo usuário. Concatene as duas tuplas e exiba a tupla resultante.

Dica: primeiro crie duas listas, e então, converta as listas em tuplas utilizando a função tuple.

Exemplo: Suplonhas que as tuplas contenham o números:
(3, 1, 5, 3, 5)
(5, 5, 7, 3, 1).
Como resultado, o programa deve gerar a tupla:
(3, 1, 5, 3, 5, 5, 5, 7, 3, 1). ''' 
lista1=[]
for a in range (5):
    n= int(input('Digite: '))
    lista1.append(n)
tupla1 = tuple(lista1)
lista2=[]
for a in range (5):
    n= int(input('Digite: '))
    lista2.append(n)
tupla2 = tuple(lista2)
print(tupla1)
print(tupla2)
soma = tupla1 + tupla2
print(soma)