#!/usr/bin/python3

import tkinter
import sys
from tkinter import ttk

window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=3)

lista = ['mac', 'windows', 'linux', 'ms-dos']
lista_item = tkinter.StringVar(value=lista)
listbox = tkinter.Listbox(window, height=100, listvariable=lista_item)
listbox.grid(column=0, row=0, sticky=tkinter.W)

window.mainloop()
sys.exit(0)
