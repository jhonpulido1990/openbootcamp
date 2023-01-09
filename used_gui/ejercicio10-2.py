#!/usr/bin/python3

import tkinter
from tkinter import ttk

window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

title = ttk.Label(window, text='listado de compras')
title.grid(column=1, row=0)

select1 = tkinter.StringVar()
select2 = tkinter.StringVar()
select3 = tkinter.StringVar()
select4 = tkinter.StringVar()
select5 = tkinter.StringVar()
select6 = tkinter.StringVar()

r1 = ttk.Checkbutton(window, text='huevos', variable=select1)
r2 = ttk.Checkbutton(window, text='pan', variable=select2)
r3 = ttk.Checkbutton(window, text='queso', variable=select3)
r4 = ttk.Checkbutton(window, text='leche', variable=select4)
r5 = ttk.Checkbutton(window, text='sal', variable=select5)
r6 = ttk.Checkbutton(window, text='azucar', variable=select6)

r1.grid(column=0, row=1)
r2.grid(column=1, row=1)
r3.grid(column=2, row=1)
r4.grid(column=0, row=2)
r5.grid(column=1, row=2)
r6.grid(column=2, row=2)

window.mainloop()
