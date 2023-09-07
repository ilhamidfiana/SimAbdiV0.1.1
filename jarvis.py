#!/usr/bin/env python
# coding: utf-8

#jarvis versi kw nya dah
# In[25]:
#==============================Library=========================================
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
from datetime import datetime
import threading # untuk multi-threading
from time import sleep
import requests
from openpyxl import Workbook
import webbrowser
import pyttsx3
import subprocess
import speech_recognition as sr
import pyaudio

root = Tk()
root.attributes("-fullscreen", True)
root.configure(background='black')
root.bind("<Escape>", quit)
root.bind("x", quit)
#USERNAME = 'Dr. Prof. Ilham Idfiana, AmdT, ST, MT, PhD'
USERNAME = 'Ilham Idfiana'
BOTNAME = 'Arham'
def text_to_speech(user_text):
    engine = pyttsx3.init()	
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 185)	
    engine.setProperty('voice', voices[0].id)	
    engine.say(user_text)	
    engine.runAndWait()


hour = datetime.now().hour
text_to_speech(f'Hello Sir. My Name Is {BOTNAME}')
sleep(2)
if (int(hour) >= 6) and (int(hour) < 12):
    text_to_speech(f"Good Morning. {USERNAME}")
    sleep(1)
elif (int(hour) >= 12) and (int(hour) < 16):
    text_to_speech(f"Good afternoon. {USERNAME}")
    sleep(1)
elif (int(hour) >= 16) and (int(hour) < 19):
    text_to_speech(f"Good Evening. MR {USERNAME}")
    sleep(1)
elif (int(hour) >= 19) and (int(hour) < 23):    
	text_to_speech(f"Good Night. {USERNAME}. Have a nice dream")
	sleep(1)

text_to_speech(f'Welcome Sir, {USERNAME}')
sleep(1)
text_to_speech(f"I am {BOTNAME} Your Personal Assistant Or in Bahasa Is Helper. How may I assist you sir")
sleep(1)  
text_to_speech(f'Please choose the menu Sir')


def nonton():
	text_to_speech('Sir you will open web for watch the movie')
	new = 1
	url = "https://149.56.24.226"
	webbrowser.open(url,new=new)
	text_to_speech(f'Have a nice day sir, {USERNAME}')
	sleep(5)
	text_to_speech(f'Dont forget her okay. by {BOTNAME}')

def browser():
	text_to_speech('Sir you will open web for search any site')
	new1 = 1
	url1 = "https://www.google.com"
	webbrowser.open(url1,new=new1)
	text_to_speech(f'Have a nice day sir, {USERNAME}')
	sleep(5)
	text_to_speech(f'Dont forget her okay. by {BOTNAME}')

def browser1():
	text_to_speech('Sir you will open the Facebook Apps')
	new2 = 1
	url2 = "https://www.facebook.com"
	webbrowser.open(url2,new=new2)
	text_to_speech(f'Have a nice day sir, {USERNAME}')
	sleep(5)
	text_to_speech(f'Dont forget her okay. by {BOTNAME}')

def browser2():
	text_to_speech('Sir you will open WA Whats app')
	new3 = 1
	url3 = "https://web.whatsapp.com/"
	webbrowser.open(url3,new=new3)
	text_to_speech(f'Have a nice day sir, {USERNAME}')
	sleep(5)
	text_to_speech(f'Dont forget her okay. by {BOTNAME}')

def office():
	text_to_speech('Sir you will open microsoft word')
	os.startfile (r"word.lnk")
	text_to_speech(f'Have a nice day sir, {USERNAME}')
	sleep(5)
	text_to_speech(f'Dont forget her okay. by {BOTNAME}')

def officeppt():
	text_to_speech('Sir you will open microsoft power point')
	os.startfile (r"ppt.lnk")	
	text_to_speech(f'Have a nice day sir, {USERNAME}')
	sleep(5)
	text_to_speech(f'Dont forget her okay. by {BOTNAME}')

def notepad():
	text_to_speech('Sir you will open notepad')
	os.startfile (r"nt.lnk")
	text_to_speech(f'Have a nice day sir, {USERNAME}')
	sleep(5)
	text_to_speech(f'Dont forget her okay. by {BOTNAME}')
		
def paint():
	text_to_speech('Sir you will open paint')
	os.startfile (r"pt.lnk")
	text_to_speech(f'Have a nice day sir, {USERNAME}')
	sleep(5)
	text_to_speech(f'Dont forget her okay. by {BOTNAME}')

def cmd():
	text_to_speech('Sir you will open command prompt')
	os.startfile (r"cmd.lnk")
	text_to_speech(f'Have a nice day sir, {USERNAME}')
	sleep(5)
	text_to_speech(f'Dont forget her okay. by {BOTNAME}')

def control():
	text_to_speech('Sir you will open control panel')
	os.startfile (r"control.lnk")
	text_to_speech(f'Have a nice day sir, {USERNAME}')
	sleep(5)
	text_to_speech(f'Dont forget her okay. by {BOTNAME}')	

def file():
	text_to_speech('Sir you will open file explorer')
	os.startfile (r"file.lnk")
	text_to_speech(f'Have a nice day sir, {USERNAME}')
	sleep(5)
	text_to_speech(f'Dont forget her okay. by {BOTNAME}')

def reset():
    id_entry.delete(0, END)
    
def shutdown():
	global time,regscreen,id_entry
	time = StringVar()
	text_to_speech('Sir you will Shutdown The Computer')
	sleep(2)
	text_to_speech('Please Set Time First, Sir ')
	timer()
	
	
def timer():
	global times,regscreen,id_entry
	tkinter.messagebox.showinfo("Jarvis Said", "Input Time FiRst")
	regscreen = Toplevel(root)	
	regscreen.title("Set Timer Shutdown")	
	regscreen.geometry("200x200")	
	times = StringVar()
	Label(regscreen, text="Set Second Time", bg="blue").pack()	
	Label(regscreen, text="").pack()	
	id_lable = Label(regscreen, text="Set Times In Minute / 60mnt")	
	id_lable.pack()	
	id_entry = Entry(regscreen, textvariable=times)	
	id_entry.pack()
	Label(regscreen, text="").pack()	
	Button(regscreen, text="Shutdown", width=10, height=1, bg="blue", command = st).pack()	
	Button(regscreen, text="Reset", width=10, height=1, bg="red", command = reset).pack()
	
    
def st(times):	
	
	waktu = times.get()
	ntime = str(waktu) * 60	
	subprocess.call(["shutdown", "-s", "-t", str(ntime)])	
	root.destroy()	
	os._exit(0)


def takeCommand():	
	text_to_speech(f'Sir you will switch to the voice, to assist you sir. please say anything and {BOTNAME} will help you sir.')
	r = sr.Recognizer()	
	with sr.Microphone() as source:	
		print("Listening...")	
		r.pause_threshold = 1	
		audio = r.listen(source)	
		try:	
			print("Recognizing...")	
			query = r.recognize_google(audio, language='en-in')	
			print(f"User said: {query}\n")
			text_to_speech(f'Thank you sir, you say to me is {query}, i will open it for you just wait')	
		except Exception as e:	
			print("Say that again please...")
			text_to_speech(f'Say again please sir')	
			return "None"	
	if 'turn music on' in query:
            text_to_speech(f'Very well sir , wait a minute i will open for you')
            sleep(1)
            music_dir = 'H:\\video lagu\\2011-2016\\'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[105]))
            text_to_speech(f'Please enjoy sir for music')
	elif 'what time is it' in query:
            hour = datetime.now().hour
            if (int(hour) >= 6) and (int(hour) < 12):
            	i = "morning"
            elif (int(hour) >= 12) and (int(hour) < 16):	
            	i = "afternoon"	
            elif (int(hour) >= 16) and (int(hour) < 19):	
            	i = "Evening"	
            elif (int(hour) >= 19) and (int(hour) < 23):	
            	i = "Night"
            text_to_speech(f'Thank you sir, you say to me is {query}, now is {hour} pass {i} sir')
	elif 'film' in query:
            text_to_speech(f'Very well sir , wait a minute i will open for you')
            sleep(1)
            film = 'H:\\video film\\LOTR\\'
            songs1 = os.listdir(film)
            print(songs1)
            os.startfile(os.path.join(film, songs1[4]))
            text_to_speech(f'Please enjoy sir for film')
#==============================GUI=========================================
ri = Image.open("register.png")
r = ImageTk.PhotoImage(ri)
label1 = Label(root, image=r)
label1.image = r
label1.place(x=180, y=100)
btn = Button(root, text = "Nonton Film", bd = 10, 
            width = "15", pady = 10, activebackground='green',
            activeforeground='white',
            font = "bold, 15",
            command = nonton, bg='yellow').place( x=180, y=340)
btn1 = Button(root, text = "Google search",activebackground='green', bd = 10, 
            activeforeground='white',
            width = "15", pady = 10,
            font = "bold, 15",
            command = browser, bg='yellow').place( x=180, y=430)
btn11 = Button(root, text = "facebook",activebackground='green', bd = 10, 
            activeforeground='white',
            width = "15", pady = 10,
            font = "bold, 15",
            command = browser1, bg='yellow').place( x=180, y=520)
btn12 = Button(root, text = "WA",activebackground='green', bd = 10, 
            activeforeground='white',
            width = "15", pady = 10,
            font = "bold, 15",
            command = browser2, bg='yellow').place( x=180, y=610)
btn12 = Button(root, text = "Voice ya",activebackground='green', bd = 10, 
            activeforeground='white',
            width = "15", pady = 10,
            font = "bold, 15",
            command = takeCommand, bg='yellow').place( x=180, y=700)

ai = Image.open("attendance.png")
a = ImageTk.PhotoImage(ai)
label2 = Label(root, image=a)
label2.image = a
label2.place(x=600, y=100)            
btn4 = Button(root, text = "Paint",activebackground='green', bd = 10, 
            activeforeground='white',
            width = "15", pady = 10,
            font = "bold, 15",
            command = paint, bg='yellow').place( x=600, y=340)
btn5 = Button(root, text = "Notepad",activebackground='green', bd = 10, 
            activeforeground='white',
            width = "15", pady = 10,
            font = "bold, 15",
            command = notepad, bg='yellow').place( x=600, y=430)
btn6 = Button(root, text = "Control Panel",activebackground='green', bd = 10, 
            activeforeground='white',
            width = "15", pady = 10,
            font = "bold, 15",
            command = control, bg='yellow').place( x=600, y=520)
btn7 = Button(root, text = "Command prompt",activebackground='green', bd = 10, 
            activeforeground='white',
            width = "15", pady = 10,
            font = "bold, 15",
            command = cmd, bg='yellow').place( x=600, y=610)
btn8 = Button(root, text = "File explorer",activebackground='green', bd = 10, 
            activeforeground='white',
            width = "15", pady = 10,
            font = "bold, 15",
            command = file, bg='yellow').place( x=600, y=700)


vi = Image.open("verifyy.png")
v = ImageTk.PhotoImage(vi)
label3 = Label(root, image=v)
label3.image = v
label3.place(x=980, y=100)
btn2 = Button(root, text = "Word",activebackground='green', bd = 10, 
            activeforeground='white',
            width = "15", pady = 10,
            font = "bold, 15",
            command = office, bg='yellow').place( x=980, y=340)

btn3 = Button(root, text = "Office",activebackground='green', bd = 10, 
            activeforeground='white',
            width = "15", pady = 10,
            font = "bold, 15",
            command = officeppt, bg='yellow').place( x=980, y=440)
btn13 = Button(root, text = "Shutdown",activebackground='green', bd = 10, 
            activeforeground='white',
            width = "15", pady = 10,
            font = "bold, 15",
            command = shutdown, bg='yellow').place( x=980, y=540)
def quit(*args):	
	text_to_speech('Thank you sir for using jarvis AI. Hope we can see again. Just press bat to open again sir')	
	root.destroy()	
	os._exit(0)
r=Button(root, text="EXIT", bd=10, 
    command=quit, font=('times new roman',12),bg="black",fg= "yellow", height=2, width= 10).place( x=1000, y=700)
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