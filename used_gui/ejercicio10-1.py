#!/usr/bin/python3

import tkinter
from tkinter import ttk

window = tkinter.Tk()

window.columnconfigure(0, weight=3)
window.columnconfigure(1, weight=3)

def limpiar(event):
    select1.set(None)
    select2.set(None)
    select3.set(None)

select1 = tkinter.StringVar()
select2 = tkinter.StringVar()
select3 = tkinter.StringVar()

r1 = ttk.Radiobutton(window, text='select=1', value=1, variable=select1)
r2 = ttk.Radiobutton(window, text='select=2', value=2, variable=select1)

r3 = ttk.Radiobutton(window, text='select=3', value=3, variable=select2)
r4 = ttk.Radiobutton(window, text='select=4', value=4, variable=select2)

r5 = ttk.Radiobutton(window, text='select=5', value=5, variable=select3)
r6 = ttk.Radiobutton(window, text='select=6', value=6, variable=select3)


r1.grid(column=0, row=1, padx=5, pady=5)
r2.grid(column=0, row=2, padx=5, pady=5)
r3.grid(column=0, row=3, padx=5, pady=5)
r4.grid(column=1, row=1, padx=5, pady=5)
r5.grid(column=1, row=2, padx=5, pady=5)
r6.grid(column=1, row=3, padx=5, pady=5)

buton = tkinter.Button(window, text='reset')
buton.grid(column=1, row=4)
buton.bind('<Button-1>', limpiar)

window.mainloop()
