def soma_divisores(n):
    cont = 1
    soma = 0
    while cont <= n:
        if (n % cont) == 0:
            soma = cont + soma
        cont+=1
    return soma
n = int(input('Digite um numero: '))
print('Resultado: ', soma_divisores(n))