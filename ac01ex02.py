def substituir(a, b, c):
    list(a)
    while b in a:
        posisacao = a.index(b)
        a[posisacao] = c
    return a
