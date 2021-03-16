'''
Preencha uma lista com 10 números digitados pelo usuário e exiba:
a - o maior número da lista
b - o menor número da lista
c - a quantidade de números pares contidos na lista
d - a média dos números contidos na lista
e - todos os números menores do que a média calculada no item anterior
'''
lista = []
for a in range(10):
    n = int(input("Numero: "))
    lista.append(n)
print(lista)
maior = max(lista)
print('Maior:', maior)
menor = min(lista)
print('Menor:', menor)
cont = 0
for a in lista:
    if a % 2 == 0:
        cont += 1
print('Quantidade de pares: ', cont)
media = sum(lista) / len(lista)
print('Media: ', media)
print('Numeros menores que a media:')
for a in lista:
    if a < media:
        print(a)