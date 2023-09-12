#from tkinter import *
import tkinter as tk
import sqlite3
import os
from PIL import ImageTk, Image
from bs4 import BeautifulSoup
import requests
import time
import datetime as dt
from sense_emu import SenseHat

#os.system('cls')

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

while True:
    

    B=(0,0,255)
    R=(255,0,0)
    G=(0,255,0)
    W=(255,255,255)
    K=(0,0,0)
    Y=(255,255,0)
    O=(255,165,0)
    Cy=(0,255,255)
    '''
    smile=[
        K,K,K,K,K,K,K,K,
        K,K,Y,Y,Y,Y,K,K,
        K,Y,B,Y,Y,B,Y,K,
        K,Y,Y,Y,Y,Y,Y,K,
        K,Y,B,Y,Y,B,Y,K,
        K,Y,Y,B,B,Y,Y,K,
        K,K,Y,Y,Y,Y,K,K,
        K,K,K,K,K,K,K,K
        ]

    sad=[
        K,K,K,K,K,K,K,K,
        K,K,Y,Y,Y,Y,K,K,
        K,Y,B,Y,Y,B,Y,K,
        K,Y,Y,Y,Y,Y,Y,K,
        K,Y,Y,B,B,Y,Y,K,
        K,Y,B,Y,Y,B,Y,K,
        K,K,Y,Y,Y,Y,K,K,
        K,K,K,K,K,K,K,K
        ]

    meeh=[
        K,K,K,K,K,K,K,K,
        K,K,Y,Y,Y,Y,K,K,
        K,Y,B,Y,Y,B,Y,K,
        K,Y,Y,Y,Y,Y,Y,K,
        K,Y,B,B,Y,Y,Y,K,
        K,Y,Y,Y,B,B,Y,K,
        K,K,Y,Y,Y,Y,K,K,
        K,K,K,K,K,K,K,K
        ]
        '''

    slika=[
        K,K,K,K,K,K,K,K,
        K,K,K,K,K,K,K,K,
        K,K,K,K,K,K,K,K,
        K,K,K,K,K,K,K,K,
        K,K,K,K,K,K,K,K,
        K,K,K,K,K,K,K,K,
        K,K,K,K,K,K,K,K,
        K,K,K,K,K,K,K,K
        ]

    '''
    tlak=sense.get_pressure()

    if tlak<1000:
        sense.set_pixels(sad)
        slika=sad
    elif tlak<1026:
        sense.set_pixels(meeh)
        slika=meeh
    else:
        sense.set_pixels(smile)
        slika=smile
        
    #time.sleep(3)
    '''

    temperature=round(sense.get_temperature(), 0)
    temperature2=round(sense.get_temperature(), 1)

    if temperature > 40:
        b=0
        while b<64:
            slika[b] = R
            b+=8
            
    elif temperature > 30:
        b=8
        while b<64:
            slika[b] = R
            b+=8
            
    elif temperature > 20:
        b=16
        while b<64:
            slika[b] = O
            b+=8
            
    elif temperature > 10:
        b=24
        while b<64:
            slika[b] = G
            b+=8
            
    elif temperature > 0:
        b=32
        while b<64:
            slika[b] = Cy
            b+=8
            
    elif temperature > -10:
        b=40
        while b<64:
            slika[b] = B
            b+=8
            
    elif temperature > -20:
        b=48
        while b<64:
            slika[b] = W
            b+=8
            
    else:
        b=56
        while b<64:
            slika[b] = W
            b+=8
            
    vlaga=sense.get_humidity()

    if vlaga > 80:
        c=7
        while c<64:
            slika[c] = B
            c+=8
            
    elif vlaga > 70:
        c=15
        while c<64:
            slika[c] = B
            c+=8
            
    elif vlaga > 60:
        c=23
        while c<64:
            slika[c] = B
            c+=8
            
    elif vlaga > 50:
        c=31
        while c<64:
            slika[c] = G
            c+=8
            
    elif vlaga > 40:
        c=39
        while c<64:
            slika[c] = G
            c+=8
            
    elif vlaga > 30:
        c=47
        while c<64:
            slika[c] = G
            c+=8
            
    elif vlaga > 20:
        c=55
        while c<64:
            slika[c] = Y
            c+=8
            
    else:
        c=63
        while c<64:
            slika[c] = Y
            c+=8
        
    sense.set_pixels(slika)

    time.sleep(1)


    gradovi = fetch_data()
    last_updated = dt.datetime.now()
    popis_gradova = timed_data()

    #temp_out=27.8
    temp_in=temperature2
    #hum_out=75
    hum_in=vlaga
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
    image_frame3=tk.Label(frame3, image=image3, text=f'{nl}{nl.join(prik)}', fg='orange', font=("Arial", 25, 'bold'), compound='center').place(x=0, y=0)

    frame4=tk.Frame(master, width=250, height=250, background="Black")
    frame4.grid(row=1, column=1)

    if temperature2 >= 22:
        image4=tk.PhotoImage(file='t-shirt2.png')
    elif temperature2 >= 12:
        image4=tk.PhotoImage(file='jacket2.png')
    elif temperature2 >= 0:
        image4=tk.PhotoImage(file='winter jacket2.png')
    elif temperature2 < 0:
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