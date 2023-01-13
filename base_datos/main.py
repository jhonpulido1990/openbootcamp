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
    mi_cursor.execute("select * from Alumnos where users = 'paola';")
    for bd in mi_cursor:
        print(bd)
    mi_cursor.close()

def crear_user(mi_conexion, users, passwd):
    mi_cursor = mi_conexion.cursor()
    mi_cursor.execute('create table if not exists Alumnos (id int primary key, users varchar(255), passwd varchar(255));')
    mi_cursor.execute('alter table Alumnos modify column id int AUTO_INCREMENT;')
    mi_cursor.execute("insert into Alumnos (users, passwd) values (%s, %s);", (users, passwd))
    mi_conexion.commit()
    mi_cursor.close()


if __name__ == '__main__':
    u = input('introduce ususario: ')
    c = getpass.getpass('introduce contraseña: ')
    mi_conexion = conectarse(u, c)
    if mi_conexion:
        crear_user(mi_conexion, 'caterine', 'dato1')
        crear_user(mi_conexion, 'paola', 'dato2')
        crear_user(mi_conexion, 'julia', 'dato3')
        crear_user(mi_conexion, 'maria', 'dato4')
        crear_user(mi_conexion, 'andrea', 'dato5')
        crear_user(mi_conexion, 'catalina', 'dato6')
        crear_user(mi_conexion, 'alexandra', 'dato7')
        crear_user(mi_conexion, 'karolina', 'dato8')
        hacer_conasulta(mi_conexion)
        desconectarse(mi_conexion)
