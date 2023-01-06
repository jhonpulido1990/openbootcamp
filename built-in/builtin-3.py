#!/usr/bin/python3

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def mifuncion(x):
    if x % 2 == 0:
        return True
    return False

resultado = filter(mifuncion, numeros)
print(list(resultado))

resultado = filter(lambda x: x % 2 == 0, numeros)
print(list(resultado))

def otherfuntion(x):
    if str(x).startswith('pep'):
        return True
    return False

resultado = filter(otherfuntion, ['pepe', 'pepito', 'juan'])
print(list(resultado))

resultado = filter(lambda x: str(x).startswith('pep'), ['pepe', 'pepito', 'juan'])
print(list(resultado))

def cuadrado(x):
    return x * x

result = map(cuadrado, numeros)
print(list(result))

result = map(lambda x: x * x, numeros)
print(list(result))
