#!/usr/bin/python3

from abc import ABC, abstractmethod

class Alumno(ABC):
    nota = 0
    nombre = ''

    @abstractmethod
    def notalumno(self):
        pass

class notasAlumno(Alumno):
    def notalumno(self):
        print('el nombre del alumno es {} y tiene una nota de {}'.format(self.nombre, self.nota))

    def califica(self):
        notacion = self.nota
        if notacion >= 3:
            print('el alumno {} pasa la materia con exito con una calificacion de {}'.format(self.nombre, self.nota))
        else:
            print('el alumno {} no pasa la materia con una calificacion de {}'.format(self.nombre, self.nota))

pepe = notasAlumno()
pepe.nombre = 'pepe'
pepe.nota = 4
pepe.notalumno()
pepe.califica()

ana = notasAlumno()
ana.nombre = 'ana'
ana.nota = 2
ana.notalumno()
ana.califica()
