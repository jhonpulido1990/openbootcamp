#!/usr/bin/python3

class dino:
    encendido = True

    def enciende():
        pass

d = dino()
d.encendido = False
print(d.encendido)

'''modo proteguido'''

class dino1:
    '''modo protegido para modo privativo son dos guion bajo'''
    _encendido = True

    def encendido(self):
        self._encendido = True

    def apaga(self):
        self._encendido = False

    def isencendido(self):
        return self._encendido

d1 = dino1()
d1.apaga()
print(d1.isencendido())

d2 = dino1()
d2.encendido()
print(d2.isencendido())


'''clases estaticas'''

class estatica:
    numero = 1

    def incrementa():
        estatica.numero += 1

print(estatica.numero)
estatica.incrementa()
print(estatica.numero)

estatica.incrementa()
print(estatica.numero)

estatica.incrementa()
print(estatica.numero)