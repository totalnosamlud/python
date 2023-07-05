import random
import os
import tkinter as tk

os.system('cls')

def izvuci_brojeve(broj_izvucenih=5, ukupni_broj=39):
    lista_izvucenih_brojeva=[]
    while(len(lista_izvucenih_brojeva)<broj_izvucenih):
        slucajni=random.randint(1,ukupni_broj)
        if slucajni not in lista_izvucenih_brojeva:
            lista_izvucenih_brojeva.append(slucajni)
    return lista_izvucenih_brojeva

def izvuci_brojeve2(broj_izvucenih2=1, ukupni_broj2=10):
    lista_izvucenih_brojeva2=[]
    while(len(lista_izvucenih_brojeva2)<broj_izvucenih2):
        slucajni2=random.randint(1,ukupni_broj2)
        if slucajni2 not in lista_izvucenih_brojeva2:
            lista_izvucenih_brojeva2.append(slucajni2)
    return lista_izvucenih_brojeva2

izvuceni_brojevi=izvuci_brojeve()
izvuceni_brojevi.sort()
izvucen_dopunski_broj=izvuci_brojeve2()

print(izvuceni_brojevi)
print(izvucen_dopunski_broj)



Lutrija=tk.Tk()
Lutrija.geometry('1200x400')
#image_in_label = tk.PhotoImage(file="EJP.jpg").subsample(7)
frame = tk.Frame(Lutrija)
frame.pack()

Lutrija.title('Generator Eurojackpot')

br1=izvuceni_brojevi[0]
br2=izvuceni_brojevi[1]
br3=izvuceni_brojevi[2]
br4=izvuceni_brojevi[3]
br5=izvuceni_brojevi[4]
dop_br=izvucen_dopunski_broj[0]

var=tk.StringVar()
var.set('Generator Eurojackpot')
frame1=tk.Frame(Lutrija)
frame1.pack(side='top')
label=tk.Label(frame1,textvariable=var,font=('Segui UI',28),width=24)
label.pack(side='top')

frame7=tk.Frame(Lutrija)
frame7.pack(side='top')
label4=tk.Label(frame7)
label4.pack()

frame2=tk.Frame(Lutrija)
frame2.pack(side='top')
tekst1=tk.Entry(frame2, bd=5,font=('Arial',28),justify='center',width=10, bg='#FFD700')
tekst1.insert(0, br1)
tekst1.pack(side='left')
tekst2=tk.Entry(frame2, bd=5,font=('Arial',28),justify='center',width=10)
tekst2.insert(0, br2)
tekst2.pack(side='left')
tekst3=tk.Entry(frame2, bd=5,font=('Arial',28),justify='center',width=10)
tekst3.insert(0, br3)
tekst3.pack(side='left')
tekst4=tk.Entry(frame2, bd=5,font=('Arial',28),justify='center',width=10)
tekst4.insert(0, br4)
tekst4.pack(side='left')
tekst5=tk.Entry(frame2, bd=5,font=('Arial',28),justify='center',width=10)
tekst5.insert(0, br5)
tekst5.pack(side='left')

frame6=tk.Frame(Lutrija)
frame6.pack(side='top')
label3=tk.Label(frame6)
label3.pack()

frame3=tk.Frame(Lutrija)
frame3.pack(side='top')
tekst6=tk.Entry(frame3, bd=5,font=('Arial',28),justify='center',width=10,bg='#FF0000',fg='white')
tekst6.insert(0, dop_br)
tekst6.pack(side='left')

frame4=tk.Frame(Lutrija)
frame4.pack(side='top')
label2=tk.Label(frame4)
label2.pack()

frame5=tk.Frame(Lutrija)
frame5.pack(side='top')
tipka=tk.Button(frame5, text='GENERIRAJ PONOVO',font=('Arial',14),command=izvuci_brojeve)
tipka.pack(side='left')
label2=tk.Label(frame5)
label2.pack(side='left')
tipka2=tk.Button(frame5, text='SPREMI KOMBINACIJU',font=('Arial',14)) #,command=spremi_kombinaciju
tipka2.pack(side='left')


tk.mainloop()