#!/usr/bin/env python
# coding: utf-8

# In[25]:

from tkinter import *
# Tkinter Library GUI
from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E
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

#==============================Main GUI=========================================
root = Tk()
root.attributes("-fullscreen", True)
root.configure(background='black')
root.bind("<Escape>", quit)
root.bind("x", quit)
        
counter = 0
# variabe untuk menyimpan data checkin dan checkout
status = statusOut = False
# variabel untuk menyimpan foto checkin dan checkout
fotoIn = fotoOut = False
# inisialisasi variabel confidence dan filename
conf = 120
filename = " "
# styling the frame which helps to
# make our background stylish
def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()

# print(1)
text_to_speech('Authentication Successful! Welcome...... ')


def callback(url):
    webbrowser.open_new(url)
frame1 = Frame(root,
            bg = "blue",
            height = "200")

# plcae the widget in gui window
frame1.pack(fill = X)


frame2 = Frame(root,
            bg = "lightgreen",
            height = "1000")
frame2.pack(fill=X) 




#==============================HEADER=========================================
# styling the label which show the text
# in our tkinter window
label = Label(frame1, text = "Selamat Datang Di GUI Absensi",
            font = "bold, 20",foreground = "white",
            bg = "blue")

label.place(x = 180, y = 70)
label = Label(frame1, text = "Tampilan ini dibuat oleh CV.... Untuk melakukan absensi",
            font = "bold, 11",foreground = "white",
            bg = "blue")

label.place(x = 150, y = 120)
# untuk tata cara penggunaan jika ada
label = Label(frame1, text = "Tata cara penggunaan. Klik disini",
            font = "bold, 11",foreground = "red",
            bg = "blue")
label.place(x = 150, y = 150)
label.bind("<Button-1>", lambda e: callback("https://ilhamidfiana.blogspot.com/p/about-me.html"))#bisa diganti
label = Label(frame1, text = "Hubungi CS",
            font = "bold, 11",foreground = "black",
            bg = "blue")
label.place(x = 150, y = 180)
label.bind("<Button-1>", lambda e: tkinter.messagebox.showinfo("SIAbdi", "Wa 089654978059"))


# entry is used to enter the text
label = Label(frame2, text = "Menu Absensi.",
            font = "bold, 20",foreground = "black",
            bg = "lightgreen")
label.place(x = 150, y = 30)


#==============================Fungsi-Fungsi=========================================
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

#==============================INPUT DATA=========================================
# In[26]:
def inputface():
    wnow = datetime.datetime.now()
    dtstring1 = wnow.strftime("%Y/%m/%d, %H:%M:%S")
    tkinter.messagebox.showinfo("SIAbdi", "Input ID di Command Prompt")
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
    id1_lable = Label(regscreen, text="No Absen ")
    id1_lable.pack()
    id1_entry = Entry(regscreen, textvariable=inputan1)
    id1_entry.pack()
    nama_lable = Label(regscreen, text="Nama ")
    nama_lable.pack()
    nama_entry = Entry(regscreen, textvariable=inputan2)
    nama_entry.pack()
    nis_lable = Label(regscreen, text="Nim/Nis ")
    nis_lable.pack()
    nis_entry = Entry(regscreen, textvariable=inputan3)
    nis_entry.pack()
    Label(regscreen, text="").pack()
    Button(regscreen, text="Register", width=10, height=1, bg="blue", command = post).pack()
    Button(regscreen, text="Reset", width=10, height=1, bg="red", command = reset).pack()
    

def post():
    cam = cv2.VideoCapture(1)
    cam.set(3, 640) # set video width
    cam.set(4, 480) # set video height
    face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')# For each person, enter one numeric face id
    id_info = face_id.get()
    noabsen_info = inputan1.get()
    nama_info = inputan2.get()
    nis_info = inputan3.get()

    wnow = datetime.datetime.now()
    dtstring1 = wnow.strftime("%Y/%m/%d, %H:%M:%S")
    #memasukkan data ke database
    mydb = mysql.connector.connect(
      host="192.168.100.162",
      user="Ilham",
      password="bsqham11",
      database="pmb"
    )
    mycursor = mydb.cursor()
    wnow = datetime.datetime.now()
    dtstring1 = wnow.strftime("%Y/%m/%d, %H:%M:%S")
    print("[INFO] database connect")
                
    command = "INSERT INTO absen (Id, Nama, NIS) VALUES (%s,%s,%s);"
    values = (noabsen_info, nama_info, nis_info)
    mycursor.execute(command, values)
    mydb.commit()
    print(mycursor.rowcount, "[INFO] database connect & data ditambah")
    
    sleep(1)#delay
    #done ya Initialize individual sampling face count
    #tkinter.messagebox.showinfo("SIAbdi", "Insiasi jangan ditekan apa-apa ya \n,Inisialisasi Menangkap Muka. Lihat ke kamera dan tunggu ...")
    print("\n [INFO] Inisialisasi Menangkap Muka. Lihat ke kamera dan tunggu ...")
    
    count = 0
    #proses untuk menangkap muka untuk disave pada file .....
    while(True):
        ret, img = cam.read()
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
            count += 1
            # Save the captured image into the datasets folder 
            # folder dapat diubah sesuai keinginan, ubah pada dataset saja,jika user ialah nama fotonya bisa diubah juga sesuai keinginan
            cv2.imwrite("dataset/User." + str(id_info) + '.' +  
                        str(count) + ".jpg", gray[y:y+h,x:x+w])
            cv2.imshow('image', img)
        k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break
        elif count >= 30: # Take 30 face sample and stop video
            break# Do a bit of cleanup
    cam.release()
    tkinter.messagebox.showinfo("SIAbdi", "Data Terinput Ke Database \n, Silahkan Tekan Latih Wajah Untuk Deteksi \n, Note : Apabila sudah difoto sama registrasi semua siswa ")
    sukses()
    
    
#==============================MelatihWajah=========================================
def train():
    path = 'dataset'
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");
    # function to get the images and label data
    def getImagesWithID(path):
        imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
        faces=[]
        IDs=[]
        for imagePath in imagePaths:
            faceImg=Image.open(imagePath).convert('L');
            faceNp=np.array(faceImg,'uint8')
            ID=int(os.path.split(imagePath)[-1].split('.')[1])
            faces.append(faceNp)
            print (ID)
            IDs.append(ID)
            cv2.imshow("training",faceNp)
            cv2.waitKey(10)
        return IDs,faces

    tkinter.messagebox.showinfo("SIAbdi", "[INFO] Melatih Wajah Siswa. Tunggu ... jika sudah exit saja .....")
    print ("\n [INFO] Melatih Wajah Siswa. It will take a few seconds. Wait ...")
    Ids,faces=getImagesWithID(path)
    recognizer.train(faces,np.array(Ids))
    recognizer.write('trainer/trainer.yml')
    recognizer.save('trainer/trainer.yml')
#==============================Absen=========================================
tanggalmasuk = datetime.datetime.now().strftime('%Y-%m-%d')
current_datetime = datetime.datetime.now().strftime('%H:%M:%S')
jamkeluars = datetime.datetime.now().strftime('%H:%M:%S')
def send_to_telegram(name, message):
    apiToken = '5791933015:AAEmlDY-0gkyw5pp5A33FAiF2EwJZUZLjis'
    chatID = '635456084'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'
    message_with_datetime = f"{message} {current_datetime} "
    messagetgl = f"{tanggalmasuk}"
    message_with_name = f"Nama Anda: {name}\nTanggal Kehadiran: {messagetgl} \n{message_with_datetime}\n"
    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message_with_name})
        print(response.text)
    except Exception as e:
        print(e)
    
now = datetime.datetime.now()
if now.hour == 6 and now.hour == 7 and now.minute < 15:
    presence_status = 'HADIR'
    ruangan = 'T1'
elif now.hour == 7 and now.minute > 16 and now.minute <= 30:
    presence_status = 'TELAT'
    ruangan = 'T1'
elif now.hour == 14 and now.minute <= 30:
    presence_status = 'PULANG'
    ruangan = 'T1'
else:
    presence_status = 'ALPA'
    ruangan = 'KEL0'




                

def absen(): #tahap pengerjaan untuk input wajah ke databasenya
    
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml') # proses untuk deteksi
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade =  cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') #Di Komputer pakai ini
    font = cv2.FONT_HERSHEY_SIMPLEX
    ts = datetime.datetime.now()
    #iniciate id counter
    mydb = mysql.connector.connect(
                  host="192.168.100.162",
                  user="Ilham",
                  password="bsqham11",
                  database="pmb"
                )
    isRecordExist=1 # boolean true false
    if (isRecordExist==1) :  
        mydb = mysql.connector.connect(
          host="192.168.100.162",
          user="Ilham",
          password="bsqham11",
          database="pmb"
        )
        print("[INFO] database connect")
        tkinter.messagebox.showinfo("SIAbdi", "[INFO] databasenya terkoneksi")
        mycursor = mydb.cursor()

        mycursor.execute("SELECT id_admin,full_name,nidn FROM petugas")
        

        myresult = mycursor.fetchall() # memunculkan hasil dari koneksi database

        for x in myresult:
          print(x)
    else:
        tkinter.messagebox.showerror("SIAbdi", "[INFO] tidak konek")
    id = 0


    # names related to ids: example ==> Marcelo: id=1,  etc
    names = myresult #Jika dekat
    names1 = myresult  # Jika Jauh
   
#==============================Main camera=========================================
    # kamera ke 1
    cam = cv2.VideoCapture(1)

    # set video widht
    cam.set(3, 640) 

    # set video height
    cam.set(4, 480) 

    # Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)
#==============================Penambahan Kamera=========================================
    '''
    # kamera ke 2
    cam = cv2.VideoCapture(1)

    # set video widht
    cam.set(3, 640) 

    # set video height
    cam.set(4, 480) 

    # Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)
    '''

    # In[27]:
#==============================Tambahkan cam 2 untuk kameranya=========================================
    print('\n[Info] Tunggu 5 detik')
    sleep(5)
    while True:
        ret, img =cam.read()
        
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        
        faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize = (int(minW), int(minH)),
        #flags = cv2.cv.CV_HAAR_SCALE_IMAGE
        flags = 0
    )
#==============================Proses Absensi=========================================
        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            label, confidence = recognizer.predict(gray[y:y+h,x:x+w])
            
                    # If confidence is less them 100 ==> "0" : perfect match 
            if (confidence < 50 ): #Jaraknya harus deket = diatas 50%
                mycursor.execute("SELECT full_name FROM petugas WHERE id_admin = %s", (label,))
                name_result = mycursor.fetchone()
                if name_result: 
                    name = name_result[0]
                    confidence = "  {0}%".format(round(100 - confidence))   
    
                    cv2.putText(img, name, (x+5, y-5), font, 1, (255, 255, 255), 2)
                    cv2.putText(
                                img, 
                                str(confidence), 
                                (x+5,y+h+20), 
                                font, 
                                1, 
                                (255,255,0), 
                                1
                               )       
                
                send_to_telegram(name, f"Status Kehadiran Anda: {presence_status}. Kedatangan Anda Pukul : ")   
                data1 = mysql.connector.connect(host="192.168.100.162",user="Ilham",password="bsqham11",database="pmb")
                cek = data1.cursor()
                perintah = "INSERT INTO masuk (jam_masuk, tgl_masuk, status, id_admin, kode_ruangan) VALUES (%s,%s,%s,%s,%s);"
                hasil = (current_datetime, tanggalmasuk, presence_status, label, ruangan)
                cek.execute(perintah, hasil)
                data1.commit()
                
            elif (confidence < 50 ): #Jaraknya harus deket = diatas 50%
                mycursor.execute("SELECT full_name FROM petugas WHERE id_admin = %s", (label,))
                name_result = mycursor.fetchone()
                if name_result: 
                    name = name_result[0]
                    confidence = "  {0}%".format(round(100 - confidence))   
    
                    cv2.putText(img, name, (x+5, y-5), font, 1, (255, 255, 255), 2)
                    cv2.putText(
                                img, 
                                str(confidence), 
                                (x+5,y+h+20), 
                                font, 
                                1, 
                                (255,255,0), 
                                1
                               )       
                send_to_telegram(name, f"Status Kepulangan Anda: {presence_status}. Kepulangan Anda Pukul : ")   
                dbs = mysql.connector.connect(host="192.168.100.162",user="Ilham",password="bsqham11",database="pmb")
                ceks = dbs.cursor()
                perintah1 = "INSERT INTO keluar (jamkeluar) VALUES (jamkeluars);"
                hasil1 = (jamkeluars)
                ceks.execute(perintah1, hasil1)
                dbs.commit()

            elif (confidence >= 51 or confidence < 100): #kebalikan dari sebelumnya jadi <= 50%
                name = "Tidak Tahu Siapa Ini"  # If the ID is not found in the database
                confidence = "  {0}%".format(round(100 - confidence))
                cv2.putText(img, name, (x+5, y-5), font, 1, (0, 0, 0), 2)
                cv2.putText(
                                img, 
                                str(confidence), 
                                (x+5,y+h+20), 
                                font, 
                                1, 
                                (255,255,0), 
                                1
                               )
        
        cv2.imshow('Absensi Mahasiswa',img) 
        k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            print("\n [INFO] Exiting Program and cleanup stuff")
            tkinter.messagebox.showinfo("SIAbdi", "[INFO] Keluar dari kamera SIAbdi")
            cam.release()
            cv2.destroyAllWindows()
            break

'''
btn3 = Button(frame2, text = "Absen",
            width = "15", pady = 10,
            font = "bold, 15",
            command = cam, bg='yellow')                            
'''
#==============================GUI=========================================
ri = Image.open("register.png")
r = ImageTk.PhotoImage(ri)
label1 = Label(frame2, image=r)
label1.image = r
label1.place(x=180, y=100)
btn = Button(frame2, text = "Foto input", bd = 10, 
            width = "15", pady = 10, activebackground='green',
            activeforeground='white',
            font = "bold, 15",
            command = inputface, bg='yellow').place( x=180, y=340)

ai = Image.open("attendance.png")
a = ImageTk.PhotoImage(ai)
label2 = Label(frame2, image=a)
label2.image = a
label2.place(x=980, y=100)            
btn1 = Button(frame2, text = "Latih Wajah",activebackground='green', bd = 10, 
            activeforeground='white',
            width = "15", pady = 10,
            font = "bold, 15",
            command = train, bg='yellow').place( x=600, y=340)

vi = Image.open("verifyy.png")
v = ImageTk.PhotoImage(vi)
label3 = Label(frame2, image=v)
label3.image = v
label3.place(x=600, y=100)
btn2 = Button(frame2, text = "Absen",activebackground='green', bd = 10, 
            activeforeground='white',
            width = "15", pady = 10,
            font = "bold, 15",
            command = absen, bg='yellow').place( x=980, y=340)

def quit(*args):
    root.destroy()
    os._exit(0)
r=Button(root, text="EXIT", bd=10, 
    command=quit, font=('times new roman',12),bg="black",fg= "yellow", height=2, width= 10).place( x=637, y=700)
'''
btn3.place(x = 750,
        y = 150)
  '''               
# give a title
root.title("GUI Absensi Digital")  
root.title("GUI Absensi Digital")   
#p1 = PhotoImage(file = 'apk.png')   #logo aplikasi
#root.iconphoto(False, p1)



# we can not change the size
# if you want you can change
    
#==============================Keluar=========================================
def on_closing():
    if tkinter.messagebox.askokcancel("Keluar", "Tekan Ok Untuk Keluar"):
        root.destroy()
        os._exit(0) 

root.protocol("WM_DELETE_WINDOW", on_closing)
#==============================Start GUI=========================================
root.mainloop()