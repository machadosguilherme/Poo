texto = input('Digite um texto: ')
texto, list()
disc = {}
if 'a' in texto:
    qtd = texto.count('a')
    disc['a'] = qtd
    if 'e' in texto:
        qtd = texto.count('e')
        disc['e'] = qtd
        if 'i' in texto:
            qtd = texto.count('i')
            disc['i'] = qtd
            if 'o' in texto:
                qtd = texto.count('o')
                disc['o'] = qtd
                if 'u' in texto:
                    qtd = texto.count('u')
                    disc['u'] = qtd
print(disc)
