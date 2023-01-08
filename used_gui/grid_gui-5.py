#!/usr/bin/python3

import tkinter
import sys
from tkinter import ttk

window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

selected = tkinter.StringVar()

r1 = ttk.Radiobutton(window, text='si', value='1', variable=selected)
r2 = ttk.Radiobutton(window, text='no', value='2', variable=selected)
r3 = ttk.Radiobutton(window, text='Quizas', value='3', variable=selected)

r1.grid(column=0, row=1, padx=5, pady=5)
r2.grid(column=0, row=2, padx=5, pady=5)
r3.grid(column=0, row=3, padx=5, pady=5)

selected2 = tkinter.StringVar()

rs1 = ttk.Radiobutton(window, text='s2i', value='12', variable=selected2)
rs1.grid(column=1, row=0, padx=5, pady=5)

window.mainloop()
sys.exit(0)
