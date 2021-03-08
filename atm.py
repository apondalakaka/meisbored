from os import name
import tkinter as tk
from tkinter import Button, Grid, Tk, messagebox
import hashlib
from tkinter import ttk
import json
import datetime
import random

root = tk.Tk()
conf = {
    'font' : ('times' , 25)
}

person = None
menu = tk.Toplevel()

def read_json(file_path):
    with open(file_path , 'r') as names:
        return json.load(names)

def write_json(file_path , data):
    with open(file_path , 'w') as names:
        json.dump(data , names , indent=4)


def get_card_number():
    n = read_json('esma.json')
    if n:
        print('beyne 1000 ta 9999')
        return n[-1]['card_number'] + random.randint(1000 , 9999)
    else:
        print('beyne 7000000000 ta 60000000000')
        return random.randint(6000000000000000 , 7000000000000000)

def get_destination(card):
    names =  read_json('esma.json')
    for name in names :
        if str(name['card_number']) == card:
            return names.indx(name)
        return None





########## def Register Button############
def confirm(a=None):
    if note.tab(note.select(), "text") == "Register":
        info={}
        info["username"] = username_r.get()
        info["Password"] = sha1(password_r.get())
        info["created_at"] = created_at_()
        info["card_number"] = get_card_number()
        info["balance"] = 10000
        names_json = read_json('esma.json')
        names_json.append(info)
        write_json('esma.json' , names_json)
        messagebox.showinfo(title='Success!' , message='You Registered success')
        username_r.set('')
        password_r.set('')



def sha1(password):
    return hashlib.sha1(password.encode('utf-8')).hexdigest()


def created_at_():
    dt= datetime.datetime.now()
    return dt.strftime("%Y-%m-%d %H:%M:%S")



############################### def login button ######################
def log_in(a=None):
    if note.tab(note.select(), "text") == "Log-in":
        global person ,ind
        names = read_json('esma.json')
        for name in  names:
            if name['username'] == username_l.get():
                if name['Password']== sha1(password_l.get()):
                    root.withdraw()#این تابع رووت رو محو میکنه و deiconify هم برش میگردونه
                    menu.deiconify()
                    person = name
                    messagebox.showinfo(title='Success!' , message='You Loged-in successfully!')
                    return None
            ind +=1
        messagebox.showerror(title='Failed', message='Username or password Invalid!')
        
    

######################### withdraw ####################
def withdraw():
    def withdrawal():
        global person , ind

        amount = withdraw_amount.get()
        # persons = read_json('esma.json')
        # for p in persons:
        #     p["username"] == person["username"]
            
        if person['balance'] > amount:
            names = read_json('esma.json')
            names[ind]['balance'] -= amount
            write_json('esma.json',names)


            messagebox.showinfo(title='Success!' , message='Withdraw  successfully!!!')
        else:
            messagebox.showerror(title='Failed', message='Not enough Money!!')

    withdraw_root  = tk.Toplevel()
    withdraw_amount = tk.IntVar()
    tk.Entry(withdraw_root , textvariable=withdraw_amount , cnf=conf).grid(row=0 , column =0 , sticky=tk.E + tk.W)
    Button(withdraw_root , text='Withdraw' , cnf=conf , command=withdrawal).grid(row=1 , column= 0 , sticky=tk.E + tk.W)
    Button(withdraw_root , text='Close' , cnf=conf).grid(row=2 , column=0 , sticky=tk.E + tk.W)



######################### balance ####################
def balance():
    username_l.get()
    balance_top = tk.Toplevel()
    now = datetime.datetime.now()
    msg= now.strftime('%Y-%m-%d\n')  + now.strftime('%H:%M:%S')
    tk.Label(balance_top , text=msg , cnf=conf ).grid(row=0 , column=0)
    msg1 = 'Your balance:\n' + str(person['balance'])
    tk.Label(balance_top , text=msg1 , cnf=conf ).grid(row=1 , column=0)
    Button(balance_top , text='Close' , cnf=conf , command=balance_top.destroy).grid(row=2 , column=0)
    
    

######################### transfer ####################
def transfer():
    def transfer_money():
        global person,ind
        amount = transfer_amount.get()
        if person['balance'] > amount:
            if get_destination(des.get()):
                names = read_json('esma.json')
                names[ind]['balance'] -= amount
                names[get_destination(des.get())]['balance'] += amount
                write_json('esma.json' , names)
                messagebox.showinfo(title='Success!' , message='transferd successfully!')
            else:
                messagebox.showerror(title='Failed', message='destination not found!!')
                transfer_root.destroy()
        else:
            messagebox.showerror(title='Failed', message='Not enough Money!!')

    def validation(var,indx,mode):
        c1=len(des.get()) == 16
        c2=des.get().isdigit()
        if c1 and c2 :
            e1.config(bg='green')
        else:
            e1.config(bg='red')
    
    
    
    
    transfer_root  = tk.Toplevel()

    tk.Label(transfer_root,text='AMOUNT').grid(row=0,column = 0)
    transfer_amount = tk.IntVar()
    tk.Entry(transfer_root , textvariable=transfer_amount , cnf=conf).grid(row=0 , column =1 )
    tk.Label(transfer_root,text='DESTINATION').grid(row=1 , column =0 )
    des = tk.StringVar()
    des.trace_add('write', validation)

    e1 = tk.Entry(transfer_root, cnf=conf , textvariable= des)
    e1.grid(row=1,column=1)
    
    Button(transfer_root , text='TRANSFER' , cnf=conf , command=transfer).grid(row=2 , column= 0 )
    Button(transfer_root , text='Close' , cnf=conf,command=transfer_root.destroy).grid(row=3 , column=0 )
######################### change [pass] ####################
def change_pass():
    def call_me_change ():
        global person , ind
        if person['Password'] == sha1(for_oldies.get()):
            if sha1(fornew.get()) == sha1(fornew2.get()):
                esma = read_json('esma.json')
                esma[ind]['Password'] = sha1(fornew.get())
                write_json('esma.json' , esma)
                messagebox.showerror(title='Failed', message='password changed')
            else: 
                messagebox.showerror(title='Failed', message='not matched!')
        else:
            messagebox.showerror(title='Failed', message='wrong password!')

    tiplivil = tk.Toplevel()

    tk.Label(tiplivil,text='!old password!').grid(row=0,column = 0)
    for_oldies = tk.StringVar()
    tk.Entry(tiplivil , textvariable=for_oldies , cnf=conf).grid(row=0 , column =1 )

    tk.Label(tiplivil,text='#new password#').grid(row=2 , column =0 )
    fornew = tk.StringVar()
    tk.Entry(tiplivil , textvariable=fornew , cnf=conf).grid(row=2 , column =1 )

    tk.Label(tiplivil,text='#confrim password#').grid(row=3 , column =0 )
    fornew2 = tk.StringVar()
    tk.Entry(tiplivil , textvariable=fornew2 , cnf=conf).grid(row=3 , column =1)

    Button(tiplivil , text='CHANGE PASSWORD' , cnf=conf , command=call_me_change).grid(row=4 , column= 1 )

root = tk.Tk()


######################################################
########################## Note book #################
######################################################

note = ttk.Notebook() 
note.grid(row=0 , column=0)
register = tk.Frame(note)
login = tk.Frame(note)
note.add(register, text='Registration Form')
note.add(login , text= 'Log-in')

################# Register ###################

tk.Label(register , text='username' ).grid(row=0 , column=0)
username_r = tk.StringVar()
tk.Entry( register , textvariable=username_r).grid(row=0 , column=1)


tk.Label(register , text='password' ).grid(row=1 , column=0)
password_r = tk.StringVar()
tk.Entry( register , textvariable=password_r ,  show= '*').grid(row=1 , column=1)

b_register =tk.Button( register , text='Register' , command=confirm)
b_register.grid(row=2 , column=0 , columnspan=2,sticky=tk.W + tk.E)
b_register.bind("<Return>", confirm)
tk.Button( register , text='Cancel', command=root.destroy ).grid(row=3 , column=0 , columnspan=2, sticky=tk.W + tk.E)


##################### Login ######################
tk.Label(login, text='username' ).grid(row=0 , column=0)
username_l = tk.StringVar()
tk.Entry( login, textvariable=username_l).grid(row=0 , column=1)


tk.Label(login, text='password' ).grid(row=1 , column=0)
password_l = tk.StringVar()
tk.Entry( login, textvariable=password_l , show= '*').grid(row=1 , column=1)

b_log =tk.Button( login, text='Login' , command=log_in)
b_log.grid(row=2 , column=0 , columnspan=2,sticky=tk.W + tk.E)
b_log.bind("<Return>", log_in)

tk.Button( login, text='Cancel', command=root.destroy ).grid(row=3 , column=0 , columnspan=2, sticky=tk.W + tk.E)


######################################################
########################## Menu ######################
######################################################


tk.Button( menu, text='Balance' , command=balance).grid(row=0 , column=0 )
tk.Button( menu, text='Withdraw' , command=withdraw).grid(row=0 , column=1 )
tk.Button( menu, text='Transfer' , command=transfer).grid(row=1 , column=0)
tk.Button( menu, text='Change password' , command=change_pass).grid(row=1 , column=1 )

ind=0
menu.withdraw()
root.mainloop()