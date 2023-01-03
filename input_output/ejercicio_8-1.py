#!/usr/bin/python3

f = open('ejercicio-8.txt', 'a')

f.write('aprendiendo con open bootcamp\n')
f.write('creacion de primer archivo py interactuando con ficheros\n')

f.close()

f = open('ejercicio-8.txt', 'r')
data = f.read()
f.close()

print(data)
