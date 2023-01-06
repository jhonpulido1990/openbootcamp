#!/usr/bin/python3

from functools import reduce
try:
    array_string = input('ingresar todos los numero que desea: ').split(' ')

    def str_to_numb(x):
        if isinstance(int(x), int):
            return True
        return False

    def suma(a, b):
        return a + b

    list_number = list(filter(str_to_numb, array_string))

    array_number = []

    for num in list_number:
        array_number.append(int(num))

    number_impar = list(filter(lambda x: x % 2 != 0, array_number))
    suma_impar = reduce(suma, number_impar)
    print(suma_impar)

except:
    print([])
