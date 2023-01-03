#!/usr/bin/python3

import pickle

class Vehículo:
    motor = ''
    puertas = 0
    velocidad = 0.0

    def __init__(self, motor, puertas, velocidad) -> None:
        self.motor = motor
        self.puertas = puertas
        self.velocidad = velocidad

mazda = Vehículo('Dissel', 5, 180.5)
f = open('ejercicio_8-2.txt', 'wb')
pickle.dump(mazda, f)
f.close()

other_file = open('ejercicio_8-2.txt', 'rb')

second_mazda = pickle.load(other_file)
other_file.close()

print('el vehiculo {} tiene {} y puede ir a {} km/h'.format(second_mazda.motor, second_mazda.puertas, second_mazda.velocidad))
