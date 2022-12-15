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
        print('prende el aparato')
        self._encendido = True

    def apaga(self):
        print('apaga el aparato')
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

'''herencias'''

class potato(dino1):
    color = None
    nombre = None

    def __init__(self, nombre):
        self.color = 'verde'
        self.nombre = nombre

    def __del__(self):
        print('estoy en el destructor de la clase :', self.__class__)

    def quitaroreja(self):
        pass

    def poneroreja(self):
        pass

class dondino(dino1):
    def verescama(self):
        pass

p = potato()
p.encendido()
print(p.isencendido())
print(dir(p))

