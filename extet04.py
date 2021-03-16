alunos = {}
for i in range(5):
    try:
        ra = int(input('Digite seu RA : '))
        if ra < 1000000 or ra > 9999999:
            raise ValueError
        if ra in alunos:
            raise TypeError
        nome = input('Digite Seu Nome: ')
        alunos[ra] = nome
    except ValueError:
        print('O ra deve ter 7 digitos... ')
    except TypeError:
        ra = int(input('O ra ja existe no dicionario, tente novamente: '))