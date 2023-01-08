#!/usr/bin/python3

import tkinter
import sys
from tkinter import ttk

window = tkinter.Tk()

def salir(event):
    print('adios')
    window.quit()

def saludar(event):
    print('han hecho click en saludar')

def doble_click(event):
    print('han hecho doble click en click')

boton = tkinter.Button(window, text='haz click')
boton.pack()
boton.bind('<Button-1>', saludar)
boton.bind('<Double-1>', doble_click)

botonsalir = tkinter.Button(window, text='salir')
botonsalir.pack()
botonsalir.bind('<Button-1>', salir)

window.mainloop()
sys.exit(0)
