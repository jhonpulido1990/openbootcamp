#!/usr/bin/python3

f = open('/etc/passwd', 'r')
# r: lectura
# a: append
# w: escritura
# x: create

# t: texto
# b: binary

# +

datos = f.read(32)
f.close()

print(datos)
