cadastro = {}
for a in range(5):
    material = input('Material a ser cadastrado: ')
    preco = float(input('O preço do material: '))
    cadastro[material] = preco
for x in cadastro:
    if cadastro[x] > 50:
        print(x)
