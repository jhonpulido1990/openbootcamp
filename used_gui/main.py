#!/usr/bin/python3

import tkinter

window = tkinter.Tk()

label_saludo = tkinter.Label(window, text='hola', bg='yellow', fg='blue')
label_saludo.pack(ipadx=50, ipady=50, side='left')

label_adio = tkinter.Label(window, text='adios', bg='red', fg='white')
label_adio.pack(ipadx=50, ipady=50, side='right')

window.mainloop()
