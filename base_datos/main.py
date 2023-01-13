#!/usr/bin/python3

import mysql.connector
from mysql.connector import Error
import getpass

def conectarse(usuario, contrasenia):
    try:

        mi_conexion = mysql.connector.connect(
            host = 'localhost',
            user = usuario,
            passwd = contrasenia,
            database = 'holajhon'
        )

        if mi_conexion.is_connected():
            print('conexion exitosa')
    except Error as e:
        print(e)
    return mi_conexion

def desconectarse(mi_conexion):
    if mi_conexion:
        mi_conexion.close()
        print('conexion cerrada exitosamente')

def hacer_conasulta(mi_conexion):
    mi_cursor = mi_conexion.cursor()
    mi_cursor.execute('select * from users;')
    for bd in mi_cursor:
        print(bd)
    mi_cursor.close()


if __name__ == '__main__':
    u = input('introduce ususario: ')
    c = getpass.getpass('introduce contraseña: ')
    mi_conexion = conectarse(u, c)
    if mi_conexion:
        hacer_conasulta(mi_conexion)
        desconectarse(mi_conexion)
