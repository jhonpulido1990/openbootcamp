#!/usr/bin/python3

paises = input('ingresar paises: ')

paises = list(paises.split(' '))

list_paises = []

for pais in sorted(paises):
    list_paises.append(pais)

print(list_paises)
