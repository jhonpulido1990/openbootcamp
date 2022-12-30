#!/usr/bin/python3

numero = 511
texto = 'quijote'
otromas = 1.2

print("el numero es %d y el texto es %s y tiene %.2f" % (numero, texto, otromas))
print("el numero es {} y el texto es {} y tiene {:.2f}".format(numero, texto, otromas))
print(f'el numero es {numero} y el texto es {texto} y tiene {otromas}')

def suma(a, b):
    return a + b

print(f'el resultado de la suma es {suma(numero, numero)}')

class juguete:
    nombre = ""
    precio = 0.0

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    # salidas informales codigo de produccion
    def __str__(self) -> str:
        return f'Mi nombre es {self.nombre} y mi precio es {self.precio}'

    # salidas tecnicas codigo de depuracion o desarrollo
    def __repr__(self) -> str:
        return f'Potato({self.nombre},{self.precio})'

j1 = juguete('potato', 10.5)
print(str(j1))
print(repr(j1))
print(dir(''))

cadena = 'en un lugar de la manchA'

print(cadena.capitalize())
print(cadena.title())
print(cadena.count('a'))
print(cadena.lower().count('a'))

numero = '5'
print(numero.isdigit())
