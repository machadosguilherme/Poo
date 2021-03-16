def calcular_salario(salario):
    if salario > 2000:
        aumento = salario + salario * (7/100)
    else:
        aumento = salario + (salario * (15/100))
    return aumento

salario = int(input('Digite seu salario: '))
print('Seu novo salario com reajuste: ', calcular_salario(salario))