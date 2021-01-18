import tkinter as tk
from tkinter import Spinbox, ttk
import time
import datetime
from tkinter.constants import DISABLED , NORMAL
from threading import Thread
def to_time(seconds):
    return str(datetime.timedelta(seconds=seconds))



def start(a,b,c):
    seconds = theyseemerollin.get()
    string = to_time(seconds)
    theyseemerollin.set(seconds)
    killninis.set(string)

def start2(a,b,c):
    seconds = theyseemerollin2.get()
    string = to_time(seconds)
    theyseemerollin2.set(seconds)
    killninis2.set(string)

def timer(number,label,box):
    box.config(state=DISABLED)
    while number:
        time.sleep(1)
        number -=1
        string = to_time(number)
        label.set(string)
    box.config(state=NORMAL)



def counter():
    c = theyseemerollin.get()
    th1= Thread(target=timer ,args=(c,killninis,spinbox1))
    th1.start()
    theyseemerollin.set(0)

def counter2 ():
    c = theyseemerollin2.get()
    th2 = Thread(target=timer,args=(c,killninis2,spinbox2))
    th2.start()
    theyseemerollin2.set(0)
root = tk.Tk()

killninis = tk.StringVar()
tk.Label(root,textvariable=killninis).grid(row = 0,column = 0)
theyseemerollin = tk.IntVar()
theyseemerollin.trace('w',start)
spinbox1 = tk.Spinbox(root,textvariable=theyseemerollin ,from_=0 , to=36000)
spinbox1.grid(row=1,column= 0)
tk.Button(root,text='START IT BIOTCH',command=counter).grid(row =2 , column=0)

killninis2 = tk.StringVar()
tk.Label(root,textvariable=killninis2).grid(row = 0,column = 1)
theyseemerollin2 = tk.IntVar()
theyseemerollin2.trace('w',start2)
spinbox2=tk.Spinbox(root,textvariable=theyseemerollin2 ,from_=0 , to=36000)
spinbox2.grid(row = 1,column= 1)
tk.Button(root,text='START IT BIOTCH',command=counter2).grid(row =2 , column=1)





root.mainloop()