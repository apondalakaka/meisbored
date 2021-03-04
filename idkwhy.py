import tkinter as tk
from tkinter import Message, ttk

def check():
    print()

def r(a=None):
    if note.tab(note.select(), "text") == "Register":
        print("r")

def l(a=None):
    if note.tab(note.select(), "text") == "Log-in":
        print("l")

root = tk.Tk()
note = ttk.Notebook()
note.grid(row=0, column=0)
register = tk.Frame(note)
login = tk.Frame(note)
note.add(register, text='Register')
note.add(login, text='Log-in')

b1 = tk.Button(register, text='r', command=r)
b1.grid(row=0, column=0)
b1.bind("<Return>", r)

b2 = tk.Button(login, text='l', command=l)
b2.grid(row=0, column=0)
b2.bind("<Return>", l)

tk.Button(root, text='check', command=check).grid(row=1, column=0)

root.mainloop()