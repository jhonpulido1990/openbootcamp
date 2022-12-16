#!/usr/bin/python3

class Vehiculo:
    Color = ''
    Ruedas = 0
    Puertas = 0

class Coche(Vehiculo):
    Velocidad = 0
    Cilindrada = 0

mycoche = Coche()
mycoche.Color = 'Rojo'
mycoche.Ruedas = 4
mycoche.Puertas = 2
mycoche.Velocidad = 3000
mycoche.Cilindrada = 4

print('el coche es de color: {}'.format(mycoche.Color))
print('el coche tiene {} ruedas'.format(mycoche.Ruedas))
print('el coche tiene {} puertas'.format(mycoche.Puertas))
print('el coche puede ira a una velocidad de {} km/h'.format(mycoche.Velocidad))
print('el coche es de {} cilindraje'.format(mycoche.Cilindrada))
