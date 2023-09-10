#from tkinter import *
import tkinter as tk
import sqlite3
import os
from PIL import ImageTk, Image

os.system('cls')

temp_out=27.8
temp_in=28.7
hum_out=75
hum_in=65
press=1013

master=tk.Tk()
master.geometry("750x500")

frame1=tk.Frame(master, width=250, height=250, background="Black")
frame1.grid(row=0, column=0)

image1=tk.PhotoImage(file='temp_out4.png')
image_frame1=tk.Label(frame1, image=image1, text=temp_out, fg='black', font=("Arial", 50, 'bold'), compound='center').place(x=0, y=0)

frame2=tk.Frame(master, width=250, height=250, background="Black")
frame2.grid(row=1, column=0)

image2=tk.PhotoImage(file='hum_out4.png')
image_frame2=tk.Label(frame2, image=image2, text=hum_out, fg='black', font=("Courier", 70, 'bold'), compound='center').place(x=0, y=0)

frame3=tk.Frame(master, width=250, height=250, background="Black")
frame3.grid(row=0, column=1)

image3=tk.PhotoImage(file='press4.png')
image_frame3=tk.Label(frame3, image=image3, text=press, fg='white', font=("Arial", 50, 'bold'), compound='center').place(x=0, y=0)

frame4=tk.Frame(master, width=250, height=250, background="Black")
frame4.grid(row=1, column=1)

frame5=tk.Frame(master, width=250, height=250, background="Black")
frame5.grid(row=0, column=2)

image5=tk.PhotoImage(file='temp_in4.png')
image_frame5=tk.Label(frame5, image=image5, text=temp_in, fg='black', font=("Arial", 50, 'bold'), compound='center').place(x=0, y=0)

frame6=tk.Frame(master, width=250, height=250, background="Black")
frame6.grid(row=1, column=2)

image6=tk.PhotoImage(file='hum_in4.png')
image_frame6=tk.Label(frame6, image=image6, text=hum_in, fg='black', font=("Courier", 70, 'bold'), compound='center').place(x=0, y=0)

master.mainloop()