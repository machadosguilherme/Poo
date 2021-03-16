def fatorial(n):
    soma = n
    resultado = 0
    while n > 1:
        soma = soma * (n-1)
        n-=1
    return soma 
n = int(input('Digite um numero: '))
print('Resultado do fatorial: ', fatorial(n)) 