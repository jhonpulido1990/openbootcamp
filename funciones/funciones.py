#!/usr/bin/python3


def matematic(a = 3, b = 1, c = 1):
    def suma(a, b, c):
        print(a + b + c)

    def resta(a, b, c):
        print(a - b - c)

    suma(a, b, c)
    resta(a, b, c)

matematic(5, 4);
matematic()

'''name parameter'''

matematic(c = -3)

'parametros variables tupla'

def sumita(*args):
    print(args)
    result = 0

    for arg in args:
        result += arg
    
    print(result)

sumita(1, 2, 3, 4, 5, 5, 45, 45, 4, 5, 5, 45, 4)

'''parametros con nombre diccionario'''

def otrasuma(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key, '=', value)
    if 'opent' in kwargs and kwargs['opent'] == 'bootcamp':
        print('aprendiendo en openbootcamp')

otrasuma(a = 1, b = 2, c = 3, d = 4, e = 5, opent='bootcamp')
otrasuma(a = 1, b = 2, c = 3, d = 4, e = 5, opent='student')


'''se utiliza print por fuera de las funciones'''

def operaciones(a, b):
    return a + b, a - b, a * b, a / b

suma, resta, mult, div = operaciones(3, 4)
resultado = operaciones(3, 4)
print(suma)
print(resta)
print(mult)
print(div)
print(resultado)


def sumador(**kwargs):
    inicial = kwargs['inicial'] if 'inicial' in kwargs else 0
    '''operacion ternaria'''
    final = kwargs['final'] if 'final' in kwargs else inicial

    result = 0

    for x in range(inicial, final + 1):
        result += x

    return result

print(sumador(inicial = 15, final = 30))

'''funciones anonimas'''
anonima = lambda nombre, nombre2: print('hola', nombre, 'adios', nombre2)
anonima('pepe', 'pablo')

sumatoria = lambda x: x + x
print(sumatoria(2))
