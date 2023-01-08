#!/usr/bin/python3

import tkinter
import sys
from tkinter import ttk

window = tkinter.Tk()

def mifuncion():
    print('clicado')

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

selected = tkinter.StringVar()

checkbox = ttk.Checkbutton(window, text='acepto las condiciones', variable=selected, command=mifuncion)
checkbox.grid(row=0, column=0)

window.mainloop()
sys.exit(0)
