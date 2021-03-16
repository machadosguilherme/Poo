media = {}
for a in range(5):
    ra = int(input('Preencha seu R.A: '))
    notas = []
    for x in range(3):
        n = int(input('Digite suas notas: '))
        notas.append(n)
    media[ra] = notas
for x in media:
    soma = sum(media[x])
    midia = soma/3
    print('R.A: {} e Media: {}'.format(x, midia))
