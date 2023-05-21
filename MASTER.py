#PRINT

spol = 'M'
godina_rodjenja = 1967
drzava_rodjenja = 'HR'

print('Spol: ',spol)
print(f'Osoba je rodjena {godina_rodjenja}. godine u {drzava_rodjenja}')

ime='Petar'
prezime='Perić'
nadimak='Perinjo'

puno_ime='Puno ime i prezime {0} {2}'.format(ime,prezime,nadimak) #iz 3 parametra vuče 0 i 2 index
print(puno_ime)

print(f'\tGodine {godina_rodjenja}. \t\nje rođena osoba: {ime} {prezime}') #\t TAB \n NEW LINE

print(ord('@')) #ORD za znak u chr code

#INPUT #INPUT INT #FLOAT INT

broj1 = int(input('Unesi broj 2: '))
cijena_kwh = float(input('Unesi cijenu kWh u EUR33:'))

#LISTE

lista=[154,'text','još jedan text',3.14, True,'Pa opet tekst']
prazna_lista=[]

print(lista)
print(prazna_lista)

zadaci=['odabrati naziv liste',
        'Unijeti elemente liste',
        'Pokrenuti aktivnosti ili elementima liste']

drugi=zadaci[1] #vraća index 1, tj. drugi podatak (prvi je na indexu 0)
print(drugi)

brojevi=[1,	'b', 3,	100]
print(len(brojevi)) #print količine podataka u listi

popis=[1,1,3,3,3,'b']
print(popis.count(1)) #koliko puta 1 u listi
print(popis.count(3))
print(popis.count('b')) #koliko puta b u listi

brojevi=[]
for broj in range(0,21):
    brojevi.append(broj)

print(brojevi)

brojevi[3]=15 # 4 poziciju, tj. index 3, mijenjamo vrijednost u 15
prvo_pojavljivanje_15=brojevi.index(15)
drugo_pojavljivanje_broja_15=brojevi[prvo_pojavljivanje_15+1:].index(15)#uvećavamo vrijednost prvog indexa da bi dobili drugo pojavljivanje

brojevi.insert(11,15) #na mjesto indexa 11 dodajemo vrijednost 15

brojevi_index_broja_15=brojevi.index(15) #pronalazi prvi 15 na listi i vraća 3 kao poziciju tj. index na kojem se nalazi

brojevi_kopija=brojevi.copy() #kopiramo sve vrijednosti liste u drugu listu

brojevi.clear() #brišemo sve vrijednosti u listi

rijeci = ['Python','Algebra','Programiranje']
brojevi.extend(rijeci) #dodajemo tri riječi na listu
brojevi_index_rijeci_Python=brojevi.index('Python') #vraća 21, tj. index na kojem se nalati riječ Python
brojevi[brojevi_index_rijeci_Python]='Java'#index 21 mijenja u Java

brojevi.insert(11,rijeci) #na mjesto indexa 11 dodaje cijelu listu tj. rijeci

print(brojevi[10]) #vraća 10 tj. vrijednost na indexu 10
print(brojevi[11][2]) # vraća Prgramiranje, tj. na indexu 11, vraća index 2 dodane liste na listu

brojevi.reverse() #obnuti poredak liste

brojevi[11].reverse() #obnuto lista na indexu 11

rijeci.sort(reverse=True) #sortira listu, u ovom slučaju descending

test_lista=[[1,2],[3,4],[5,6]]
for podlista in test_lista:
    podlista.reverse() #obnuto liste u listi
test_lista.reverse() #obnuta cijela lista

#FOR PETLJA

brojevi=[1,	2,	3,	4,	5,	6,	7,	8,	9,	10]
for broj in brojevi:
    print('Broj',broj,sep='_',end=' ') #Broj_1 Broj_2 tj. SEP za seprator, END za kraj reda, tj. u ovom slučaju da ne ide u novi red

mixed=[10, 3.14, 5, 7.43]
sum=0
print(mixed)
for element in mixed:
    sum=sum+element #uvećavamo sum za vrijednost elementa
    print(round(sum,2)) #round na dvije decimnale

for broj in range(1,11,3):
    print(broj,end=' ') #vraća 1 4 7 10, počinjemo sa 1, završavamo sa 11, step je 3

djeljivi_sa_7=[]
for broj7 in range(0,101,7):
    djeljivi_sa_7.append(broj7) #dodajemo vrijednost na listu
    print(broj7,end=' ')

granica = int(input('Unesi gornju granicu'))
for broj2 in range(granica): #koristimo unesenu vrijednost kao range for petlje
    print(broj2,end=' ')

for i in brojevi:
    print(i, end=' ')
    sum+=i #dodajemo +1 ili neku vrijednost na ovaj način
    #paziti da se radi o istom tipovima podataka ako imamo npr. matematičke operatore

#IF: ELIF; ELSE

brojevi=[]

for broj in range(1,31):
    brojevi.append(broj)

for broj in brojevi:
    if broj%9 == 0 and broj%6 == 0:
        print(f'Broj {broj} je djeljiv sa 3, 6 i 9')
    elif broj%9 == 0:
        print(f'Broj {broj} je djeljiv sa 3 i 9')
    else:
        print(f'Broj {broj} nije djeljiv sa 3, 6 ili 9')

#SLICE LISTE ?

brojevi=[]
for broj in range(0, 101):
    brojevi.append(broj)

#print(brojevi)
izdvojeni_brojevi = brojevi[5:(19+1):2] #[5, 7, 9, 11, 13, 15, 17, 19] #dodajemo +1 radi toga što indexi počinju sa 0
print(izdvojeni_brojevi)

#SLICE ?

rijec=input('Unesite riječ za koju mislite da je palindrom')
obrnuta_rijec=rijec[::-1]

#DICTIONARY

stanovnistvo={
    '12345678901':'Petar Perić',
    '31454545456':['Marko Marić', 'proba'],
    '31454567456':'Ivan Ivić',
    '95354567456':'Josip Josipović'
}

element=stanovnistvo['12345678901'] #Petar Perić
element2=stanovnistvo['31454545456'] #['Marko Marić', 'proba'] --> vraća listu koja je dio dictionary za drugu osobu

stanovnistvo['95354567456']= 'Mate Matić'#Mato Matić dodijeljuje umjesto Ivan Ivić

for kljuc in stanovnistvo.keys():
    print(kljuc, end='; ') #12345678901; 31454545456; 31454567456; 95354567456; 

for vrijednosti in stanovnistvo.values():
    print(vrijednosti, end='; ') #Petar Perić; ['Marko Marić', 'proba']; Ivan Ivić; Josip Josipović;

for key, value in stanovnistvo.items():
    print(key, value, end='; ') #12345678901 Petar Perić; 31454545456 ['Marko Marić', 'proba']; 31454567456 Ivan Ivić; 95354567456 Josip Josipović;

#DICTIONARY WITH LIST

vozni_park = {
    1 : ['Kamion', 'Iveco', 'OS 001 ZZ', 2015, 45000.00],
    2 : ['Kamion', 'Iveco', 'OS 002 ZZ', 2015, 47000.00],
} 

header_top=f'ID\tTip\t\tProizvodjac\t\tRegistarska\t\tGodina prve\t\tCijena'
header_bottom=f' \t   \t\t          \t\toznaka\t\t\tregistracije\t\t(EUR)' 
header_underline='_'*110

print(header_top)
print(header_bottom)
print(header_underline)

for key, value in vozni_park.items():
    print(f'{key}', end='\t') #printa 1 i ispod 2
    for element in value:
        print(f'{element}', end='\t\t') #u nastavku prethodnog printa printa podatke
    print()

vrijednost_1=vozni_park.pop(1,'neće se ni vratiti') #briše i vrača vrijednost izbrisanog, text se neće vratiti jer postoji na listi i obrisan je
vrijednost_10=vozni_park.pop(10,'Nema takvog vozila') #vraća Nema takvog vozila jer nema 10 na listi

vrijednost_7=vozni_park.popitem() #briše zadnji zapis 

print(vrijednost_7) #(8, ['Dostavno vozilo', 'Volkswagen', 'ZG 002 ZZ', 2010, 9300.0])
print(vrijednost_7[0]) #8
print(vrijednost_7[1]) #['Dostavno vozilo', 'Volkswagen', 'ZG 002 ZZ', 2010, 9300.0]
print(f'tablica je {vrijednost_7[1][2]}') #tablica je ZG 002 ZZ

#WHILE PETLJA

broj = 0
while broj < 10:
    print(broj , end = ' ')
    broj += 1

#BREAK, CONTINUE

for broj in range (10):
    if broj%2==0:
        continue #uvjet ispunjenjen preskoći ostatak koda i vrati se na početak uvjeta ili petlje
    print(broj, end=' ')

for broj in range (1,10):
    if broj%6==0:
        break #uvjet ispunjenjen preskoći ostatak koda u bloku i nastavi izvršavanje izvan petlje
    print(broj, end=' ')

####stao na zad22


