#!/usr/bin/python3

def divicion(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'no se puede dividir por zero'
