from tkinter import *
# Tkinter Library GUI
import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox
import sys
import pandas as pd
from bs4 import BeautifulSoup
from pathlib import Path
import xlsxwriter
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn
from scipy.stats import mode
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from PIL import ImageTk,Image
import cv2
import numpy as np
import os 
import sqlite3
import mysql.connector
import pymysql
import imutils
from imutils.video import VideoStream # untuk video stream
from imutils.video import FPS
import time
import datetime
import threading # untuk multi-threading
from time import sleep
import requests
from openpyxl import Workbook
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
ID = StringVar()
EMAIL = StringVar()

def sukses():
    global login_success_screen
    login_success_screen = Toplevel(regscreen)
    login_success_screen.title("Success")
    login_success_screen.geometry("250x200")
    Label(login_success_screen, text="Data Terinput Ke Database \n, Silahkan Tekan Latih Wajah Untuk Deteksi \n, Note : Apabila sudah difoto sama registrasi semua siswa").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
def delete_login_success():
    login_success_screen.destroy()
def reset():
    id_entry.delete(0, END)
    id1_entry.delete(0, END)
    nama_entry.delete(0, END)
    nis_entry.delete(0, END)

def inputface():
    wnow = datetime.datetime.now()
    dtstring1 = wnow.strftime("%Y/%m/%d, %H:%M:%S")
    tkinter.messagebox.showinfo("SIAbdi", "Daftar dulu")
    global regscreen
    regscreen = Toplevel(root)
    regscreen.title("Register")
    regscreen.geometry("300x300")
    global face_id,inputan1,inputan2,inputan3,id1_entry,id_entry,nama_entry,nis_entry
    face_id = StringVar()
    inputan1 = StringVar()
    inputan2 = StringVar()
    inputan3 = StringVar()
    Label(regscreen, text="Menu Register", bg="blue").pack()
    Label(regscreen, text="").pack()
    id_lable = Label(regscreen, text="ID")
    id_lable.pack()
    id_entry = Entry(regscreen, textvariable=face_id)
    id_entry.pack()
    id1_lable = Label(regscreen, text="Username ")
    id1_lable.pack()
    id1_entry = Entry(regscreen, textvariable=inputan1)
    id1_entry.pack()
    nama_lable = Label(regscreen, text="Email ")
    nama_lable.pack()
    nama_entry = Entry(regscreen, textvariable=inputan2)
    nama_entry.pack()
    nis_lable = Label(regscreen, text="Password ")
    nis_lable.pack()
    nis_entry = Entry(regscreen, textvariable=inputan3)
    nis_entry.pack()
    Label(regscreen, text="").pack()
    Button(regscreen, text="Register", width=10, height=1, bg="blue", command = Database).pack()
    Button(regscreen, text="Reset", width=10, height=1, bg="red", command = reset).pack()

def Database():
    global USERNAME, PASSWORD, ID, PASSWORD
    ID = face_id.get()
    USERNAME = inputan1.get()
    EMAIL = inputan2.get()
    PASSWORD = inputan3.get()
    #memasukkan data ke database
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="ninja"
    )
    mycursor = mydb.cursor()
    print("[INFO] database connect")
    tkinter.messagebox.showinfo("SIAbdi", "[INFO] database connect")
                
    command = "INSERT INTO data (Id, Username, Email, Password) VALUES (%s,%s,%s,%s);"
    values = (ID, USERNAME, EMAIL, PASSWORD)
    mycursor.execute(command, values)
    mydb.commit()
    print(mycursor.rowcount, "[INFO] database connect & data ditambah")
    tkinter.messagebox.showinfo("SIAbdi", "Data Terinput Ke Database ")
    sleep(1)

        
def Login(event=None):	
	global USERNAME, PASSWORD, ID, EMAIL
	global face_id,inputan1,inputan2,inputan3,id1_entry,id_entry,nama_entry,nis_entry	
	mydb = mysql.connector.connect(	
      host="localhost",	
      user="root",	
      password="",	
      database="ninja"	
    )
	tkinter.messagebox.showinfo("SIAbdi", "[INFO] databasenya terkoneksi")
	mycursor = mydb.cursor()
	mycursor.execute("SELECT Id, Username, Email, Password FROM data")
	myresult = mycursor.fetchall() # memunculkan hasil dari koneksi database
	for x in myresult:
		print(x)
		break

	if USERNAME == USERNAME or PASSWORD == PASSWORD:
		lbl_text.config(text="Betul", fg="blue")
		text_to_speech('Good GG GAMING')
		tk.messagebox.showinfo("SIAbdi", "[INFO] Login Sukses")
		call()
	else:
		lbl_text.config(text="Password Anda salah", fg="red")
		text_to_speech('Wrong Password Try Again! ')
		USERNAME.set("")
		PASSWORD.set("")   

def call():
	root.destroy()
	os.system('python game.py')            
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
lbl_title = Label(Top, text = "Ninja Ilham", bg="black", fg="green", font=('Helvetica', 64))
lbl_title.pack(fill=BOTH,expand=1)
lb_title = Label(Top, text = "", bg="black", fg="green", font=('Helvetica', 64))
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
r=Button(root, text="Register", bd=10, 
    command=inputface, font=('times new roman',12),bg="white",fg= "black", height=2, width= 10).place( x=800, y=700)


#==============================INITIALIATION==================================
# if __name__ == '__main__':
root.mainloop()