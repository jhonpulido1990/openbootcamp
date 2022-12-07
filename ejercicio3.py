#!/usr/bin/python3
peso = float(input('por favor ingresa tu peso corporal: '))
altura = float(input('por favor ingresa tu altura: '))
print('tu peso corporal es: {} kg'.format(peso))
print('tu altura es: {} metros'.format(altura))
imc = peso / (altura ** 2)
print('Tu índice de masa corporal es: {:.2f}'.format(imc))
