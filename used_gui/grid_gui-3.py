#!/usr/bin/python3

import tkinter
import sys
from tkinter import ttk

window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=3)

frame = ttk.Frame(window)

label = ttk.Label(frame, text='hola')
label.grid(column=0, row=0, sticky=tkinter.W, padx=50, pady=50)

frame.grid(column=0, row=0, sticky=tkinter.W)

window.mainloop()
sys.exit(0)
