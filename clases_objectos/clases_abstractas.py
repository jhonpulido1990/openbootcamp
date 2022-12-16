#!/usr/bin/python3

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sonido(self):
        pass

    def dihola(self):
        print('hola')

class perro(Animal):
    def sonido(self):
        print('guau')

class gato(Animal):
    def sonido(self):
        print('miau')

p = perro()
p.sonido()
p.dihola()

g = gato()
g.sonido()
g.dihola()

# has - A

class Motor:
    tipo = 'diesel'

class Ventana:
    cantidad = 5

    def cambiarCantidad(self, valor):
        self.cantidad = valor

class Rueda:
    cantidad = 4

class Carroceria:
    ventana = Ventana()
    ruedas =  Rueda()

class Coche:
    motor = Motor()
    carroceria = Carroceria()


c = Coche()
print('motor es: ', c.motor.tipo)
print('ventanas es: ', c.carroceria.ventana.cantidad)

c.carroceria.ventana.cambiarCantidad(8)
print('ventanas es: ', c.carroceria.ventana.cantidad)

