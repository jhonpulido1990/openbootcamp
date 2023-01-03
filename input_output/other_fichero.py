#!/usr/bin/python3

import pickle

class Juguete:
    nombre = ""
    precio = 0

    def __init__(self, nombre, precio) -> None:
        self.nombre = nombre
        self.precio = precio

    def getNombre(self):
        return self.nombre

j1 = Juguete('potato', 10.5)
#f = open('datos.bin', 'wb')
f = open('datos.bin', 'rb')
print(type(j1))
print(j1.getNombre())
#pickle.dump(j1, f)
potato = pickle.load(f)
f.close()

print(type(potato))
print(potato.getNombre(), 'precio es: ', potato.precio)
