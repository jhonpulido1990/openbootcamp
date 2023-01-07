#!/usr/bin/python3
import tkinter
from tkinter import ttk

window = tkinter.Tk()

# (0,0) (1,0) (2,0)
# (0,1) (1,1) (2,1)
# (0,2) (1,2) (2,2)
# ---------------------------
# label entry (2,0)
# label entry (2,1)
# (0,2) (1,2) button

window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=3)

# etiqueta usuario
user_name = ttk.Label(window, text='user_name:')
user_name.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

user_entry = ttk.Entry(window)
user_entry.grid(column=1, row=0, sticky=tkinter.E, padx=5, pady=5)

# etiqueta password
password_label = ttk.Label(window, text='password:')
password_label.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5)

password_entry = ttk.Entry(window, show='*')
password_entry.grid(column=1, row=1, sticky=tkinter.E, padx=5, pady=5)

# button
login_buton = ttk.Button(window, text='loggin')
login_buton.grid(column=1, row=3, sticky=tkinter.E, padx=5, pady=5)

window.mainloop()
