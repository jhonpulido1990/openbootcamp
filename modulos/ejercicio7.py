#!/usr/bin/python3

from calculadora.op_suma import sumando
from calculadora.op_resta import restando
from calculadora.op_multi import multiplicar
from calculadora.op_div import divicion


operador = input('ingresa la palabra suma, resta, multi o div seguido de dos numeros ejempl multi 2 3:  ')
op = {'suma': sumando, 'resta': restando, 'multi': multiplicar, 'div': divicion}

if len(operador) == 0:
    print('falta agregar argumentos')
else:
    array_string = operador.split(' ')
    if array_string[0] in op:
        if len(array_string) == 3:
            try:
                a = float(array_string[1])
                b = float(array_string[2])
                print(op[array_string[0]](a, b))
            except:
                print('uno de los argumentos no es un numero')
        else:
            print('falta agregar argumentos')
    else:
        print('no coincide con las operaciones establecidas')
