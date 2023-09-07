import tkinter as tk
from tkinter import *
import tkinter.messagebox
from PIL import ImageTk,Image
import os
import webbrowser
import pyttsx3
def quit(*args):
    root.destroy()
def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()
root = Tk()
root.attributes("-fullscreen", True)
root.configure(background='black')
root.bind("<Escape>", quit)
root.bind("x", quit)
USERNAME = StringVar()
PASSWORD = StringVar()
def Database():
    global USERNAME, PASSWORD
    
def Login(event=None):
    Database()
    if USERNAME.get() == "admin" or PASSWORD.get() == "admin":
        lbl_text.config(text="Betul", fg="blue")
        tk.messagebox.showinfo("SIAbdi", "[INFO] Login Sukses")
        call()
    else:
        lbl_text.config(text="Password Anda salah", fg="red")
        text_to_speech('Wrong Password Try Again! ')
        USERNAME.set("")
        PASSWORD.set("")   

def call():
	root.destroy()
	os.system('python Webcam.py')            
def Back():
    Home.destroy()
    root.deiconify()
   

label=Label(root)
label.pack()
Top = Frame(root, bd=10,  relief=RIDGE)
Top.pack(side=TOP, fill=X)
Faltu=Frame(root, height=500, relief=RIDGE)
Faltu.pack(side=TOP, fill=X, ipady=50, ipadx=200)
Form = Frame(root, height=50, bd=30)
Form.pack(side=TOP, pady=20)

 
#==============================LABELS=========================================
lbl_title = Label(Top, text = "Welcome to SiAbdi", bg="black", fg="green", font=('Helvetica', 64))
lbl_title.pack(fill=BOTH,expand=1)
lb_title = Label(Top, text = "FaceCam", bg="black", fg="green", font=('Helvetica', 64))
lb_title.pack(fill=BOTH,expand=1)
cre=Label(Faltu, text= "Enter your credentials: ", fg="green", bg="black", font=('Verdana',20))
cre.pack(fill=BOTH, expand=1)
cre.bind("<Button-1>", lambda e: tkinter.messagebox.showinfo("SIAbdi", "User admin pass admin \n jika ingin keluar tekan esc"))
lbl_username = Label(Form, text = "Username:", font=('arial', 14), bd=15)
lbl_username.grid(row=0, sticky="e")
lbl_password = Label(Form, text = "Password:", font=('arial', 14), bd=15)
lbl_password.grid(row=1, sticky="e")
lbl_text = Label(Form)
lbl_text.grid(row=2, columnspan=2)
 
#==============================ENTRY WIDGETS==================================
username = Entry(Form, textvariable=USERNAME, font=(14))
username.grid(row=0, column=1)
password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
password.grid(row=1, column=1)
 
#==============================BUTTON WIDGETS=================================
btn_login = Button(Form, text="Login", width=45, command=Login)
btn_login.grid(pady=25, row=3, columnspan=2)
btn_login.bind("<Return>", Login)

r=Button(root, text="EXIT", bd=10, 
    command=quit, font=('times new roman',12),bg="white",fg= "black", height=2, width= 10).place( x=537, y=700)


#==============================INITIALIATION==================================
# if __name__ == '__main__':
root.mainloop()