while True:
    try:
        x = int(input('Primeiro valor: '))
        y = int(input('Segundo valor: '))
        if x < 0 or y < 0:
            raise TypeError
        z = x / y
        print('O resultado é: ', z)
    except TypeError:
        print('O numero deve ser um positivo')
    except ZeroDivisionError:
        print('O segundo valor não pode ser zero')
    except ValueError:
        print('O numero precisa ser um inteiro.')
    except Exception:
        print('Ocorreu um erro...')
    else:
        break
    finally:
        print('O programa funcionou com sucesso...')
