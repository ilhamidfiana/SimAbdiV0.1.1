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


    tkinter.messagebox.showinfo("SIAbdi", "[INFO] Absen")
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml') # proses untuk deteksi
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade =  cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') #Di Komputer pakai ini
    font = cv2.FONT_HERSHEY_SIMPLEX
    ts = datetime.datetime.now()
    #iniciate id counter
    mydb = mysql.connector.connect(
                  host="192.168.100.168",
                  user="Ilham",
                  password="bsqham11",
                  database="facebase"
                )
    isRecordExist=1 # boolean true false
    if (isRecordExist==1) :  
        mydb = mysql.connector.connect(
          host="192.168.100.168",
          user="Ilham",
          password="bsqham11",
          database="facebase"
        )
        print("[INFO] database connect")
        tkinter.messagebox.showinfo("SIAbdi", "[INFO] databasenya terkoneksi")
        mycursor = mydb.cursor()

        mycursor.execute("SELECT Id,Nama,NIS FROM absen")
        

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
        flags = 0
    )
#==============================Proses Absensi=========================================
        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            label, confidence = recognizer.predict(gray[y:y+h,x:x+w])
            
                    # If confidence is less them 100 ==> "0" : perfect match 
            if (confidence < 100): #Jaraknya harus deket
                mycursor.execute("SELECT Nama FROM absen WHERE Id = %s", (label,))
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
                
				
                break
            else:
                name = "Unknown"  # If the ID is not found in the database
                confidence = ""            
        
        cv2.imshow('camera',img) 
        k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break# Do a bit of cleanup
    print("\n [INFO] Exiting Program and cleanup stuff")
    tkinter.messagebox.showinfo("SIAbdi", "[INFO] Keluar dari kamera SIAbdi")
    cam.release()