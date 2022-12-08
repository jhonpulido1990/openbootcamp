#!/usr/bin/python3

lista = ['hola', 'mensaje', 'adios']

for palabra in lista:
    if palabra == 'mensaje':
        print('palabra encontrada')
        break
else:
    print('no la he encontrado')

'''formas de utilizar el else en un for'''

for palabra in lista:
    if palabra == 'pedro':
        print('palabra encontrada')
        break
else:
    print('no la he encontrado')
