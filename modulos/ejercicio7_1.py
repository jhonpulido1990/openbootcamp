#!/usr/bin/python3

# Python Program to Convert seconds
# into hours, minutes and seconds

import time

# Driver program
try:
    hours = int(input('tiempo en horas: ')) * 3600
    hora = time.gmtime(hours)[3]
except:
    hora = time.localtime()[3]


restante = time.strptime("07:00"[:2],"%H")[3] - hora
if restante >= 0:
    print(f"El tiempo restante de trabajo es:  {restante} hora/s")
else:
    print('el turno de trabajo ha finalizado')
