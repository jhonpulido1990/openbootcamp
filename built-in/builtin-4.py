#!/usr/bin/python3

from functools import reduce

def suma(a, b):
    return a + b

res = reduce(suma, [1, 2, 3, 4, 5])
print(res)

res = reduce(lambda a, b: a + b, [1, 2, 3, 4, 5])
print(res)

curso = ['java', 'python', 'git']
asistentes = [15, 28, 4]

demo = zip(curso, asistentes)

print(list(demo))
