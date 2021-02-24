import tkinter as tk
from tkinter import Button, messagebox
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


########## def Register Button############
def confirm():
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
def log_in():
    global person
    names = read_json('esma.json')
    for name in  names:
        if name['username'] == username_l.get():
            if name['Password']== sha1(password_l.get()):
                root.withdraw()#این تابع رووت رو محو میکنه و deiconify هم برش میگردونه
                menu.deiconify()
                person = name
                messagebox.showinfo(title='Success!' , message='You Loged-in successfully!')
                return None
    messagebox.showerror(title='Failed', message='Username or password Invalid!')


######################### withdraw ####################
def withdraw():
    def withdrawal():
        amount = withdraw_amount.get()
        persons = read_json('esma.json')
        for p in persons:
            p["username"] == person["username"]
            
        if person['balance'] > amount:
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
    def ppress():
        ti = tk.Toplevel()
        trNSFERKN = tk.IntVar()
        Button(ti , text='transfer' , cnf=conf , command=ppress)
######################### change [pass] ####################
def change_pass():
    pass


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

tk.Button( register , text='Register' , command=confirm).grid(row=2 , column=0 , columnspan=2,sticky=tk.W + tk.E)
tk.Button( register , text='Cancel', command=root.destroy ).grid(row=3 , column=0 , columnspan=2, sticky=tk.W + tk.E)


##################### Login ######################
tk.Label(login, text='username' ).grid(row=0 , column=0)
username_l = tk.StringVar()
tk.Entry( login, textvariable=username_l).grid(row=0 , column=1)


tk.Label(login, text='password' ).grid(row=1 , column=0)
password_l = tk.StringVar()
tk.Entry( login, textvariable=password_l , show= '*').grid(row=1 , column=1)

tk.Button( login, text='Login' , command=log_in).grid(row=2 , column=0 , columnspan=2,sticky=tk.W + tk.E)
tk.Button( login, text='Cancel', command=root.destroy ).grid(row=3 , column=0 , columnspan=2, sticky=tk.W + tk.E)


######################################################
########################## Menu ######################
######################################################


tk.Button( menu, text='Balance' , command=balance).grid(row=0 , column=0 )
tk.Button( menu, text='Withdraw' , command=withdraw).grid(row=0 , column=1 )
tk.Button( menu, text='Transfer' , command=transfer).grid(row=1 , column=0)
tk.Button( menu, text='Change password' , command=change_pass).grid(row=1 , column=1 )


menu.withdraw()
root.mainloop()