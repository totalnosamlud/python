#from tkinter import *
import tkinter as tk
import sqlite3
import os
from PIL import ImageTk, Image
from bs4 import BeautifulSoup
import requests
import time
import datetime as dt
import sqlite3

os.system('cls')

#### pripremamo bazu

create_table_query='''

CREATE TABLE IF NOT EXISTS weather_logs (
    grad TEXT,
    last_updated TEXT,
    temp_out TEXT,
    temp_in TEXT,
    hum_out TEXT,
    hum_in TEXT,
    press TEXT,
    vrijeme TEXT
);
'''

database_name='WeatherStation.db'

try:
    sc=sqlite3.connect(database_name)
    cursor=sc.cursor()
    #print('Spojeni na bazu')
    cursor.execute(create_table_query)
    sc.commit()
    #print(sc)
    cursor.close()
except sqlite3.Error as err:
    print('Greška', err)
finally:
    if sc:
        sc.close()
        
        
def weather_log():
    
    insert_into_query='''
    insert into weather_logs (grad, last_updated, temp_out, temp_in, hum_out, hum_in, press, vrijeme)
    values (?,?,?,?,?,?,?,?)
    
    '''
    grad_log=[grad, last_updated, temp_out, temp_in, hum_out, hum_in, press, vrijeme]
    
    try:
        sc=sqlite3.connect(database_name)
        cursor=sc.cursor()
        #print('Spojeni na bazu')
        cursor.execute(insert_into_query, grad_log)
        sc.commit()
        #print(sc)
        cursor.close()
    except sqlite3.Error as err:
        print('Greška', err)
    finally:
        if sc:
            sc.close()
            
def read_weather_log():
    database_name='WeatherStation.db'
    sc = sqlite3.connect(database_name)
    cursor_obj = sc.cursor()
    statement = '''
    SELECT
        *
    FROM
        weather_logs

    '''
    
    cursor_obj.execute(statement)
    output = cursor_obj.fetchall()
    print(output)

def fetch_data():
 
    url = 'https://vrijeme.hr/hrvatska_n.xml'
    xml = requests.get(url)
    soup = BeautifulSoup(xml.content, 'lxml')
    gradovi = soup.find_all('grad')
    return gradovi
 
def lista_gradova(gradovi):
    popis_gradova = []
    for grad in gradovi:
        ime_grada = grad.find('gradime').text
        lat = grad.find('lat').text
        podatci = grad.find('podatci')
        popis_gradova.append((ime_grada, podatci))
 
    return popis_gradova   
 
 
def timed_data():
    global last_updated, gradovi
 
    temp_last_updated = last_updated.minute
    old = lista_gradova(gradovi)
    test = temp_last_updated//15*15%60
    last_updated = last_updated.replace(minute = test)
 
    if temp_last_updated < test or test == 0:
        last_updated = dt.datetime.now()
        temp_gradovi = fetch_data()
        timed_popis_gradova = lista_gradova(gradovi)
        print(last_updated, "if", test)
        #weather_log()
        return timed_popis_gradova
    else:
        print(last_updated,"else", test)
        timed_popis_gradova = lista_gradova(gradovi)
        #weather_log()
        return timed_popis_gradova
 
 
gradovi = fetch_data()
last_updated = dt.datetime.now()
popis_gradova = timed_data()

#temp_out=27.8
temp_in=28.7
#hum_out=75
hum_in=65
#press='1013 Hpa'
 
for grad, podatci in popis_gradova:
    if grad == 'Zagreb-Grič':
        grad_disp=grad
        temp_out = podatci.find('temp').text
        hum_out = podatci.find('vlaga').text
        press = podatci.find('tlak').text
        vrijeme = podatci.find('vrijeme').text
        print(f'{grad} {temp_out} {hum_out} {press} {vrijeme}')
        weather_log()
        break



prik=[vrijeme, press+' Hpa']
nl = '\n'

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

image3=tk.PhotoImage(file='press6.png')
image_frame3=tk.Label(frame3, image=image3, text=f'{nl}{nl.join(prik)}', fg='orange', font=("Arial", 30, 'bold'), compound='center').place(x=0, y=0)

frame4=tk.Frame(master, width=250, height=250, background="Black")
frame4.grid(row=1, column=1)

verzija_slike=2

if verzija_slike==1:
    image4=tk.PhotoImage(file='t-shirt2.png')
elif verzija_slike==2:
    image4=tk.PhotoImage(file='jacket2.png')
elif verzija_slike==3:
    image4=tk.PhotoImage(file='winter jacket2.png')
elif verzija_slike==4:
    image4=tk.PhotoImage(file='cold winter2.png')
    
image_frame3=tk.Label(frame4, image=image4, fg='orange', font=("Arial", 30, 'bold'), compound='center').place(x=0, y=0)

frame5=tk.Frame(master, width=250, height=250, background="Black")
frame5.grid(row=0, column=2)

image5=tk.PhotoImage(file='temp_in4.png')
image_frame5=tk.Label(frame5, image=image5, text=temp_in, fg='black', font=("Arial", 50, 'bold'), compound='center').place(x=0, y=0)

frame6=tk.Frame(master, width=250, height=250, background="Black")
frame6.grid(row=1, column=2)

image6=tk.PhotoImage(file='hum_in4.png')
image_frame6=tk.Label(frame6, image=image6, text=hum_in, fg='black', font=("Courier", 70, 'bold'), compound='center').place(x=0, y=0)

master.mainloop()