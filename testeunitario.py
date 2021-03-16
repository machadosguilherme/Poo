from extet05 import converte_para_fahrenheit
try:
    c = converte_para_fahrenheit(95)
    assert c == 203.0
    print('correto')
except AssertionError:
    print('Erro')
    print('Retorno ', c)
