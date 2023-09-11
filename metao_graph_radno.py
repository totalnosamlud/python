from sense_emu import SenseHat
import time
sense = SenseHat()

while True:

    B=(0,0,255)
    R=(255,0,0)
    G=(0,255,0)
    W=(255,255,255)
    K=(0,0,0)
    Y=(255,255,0)
    O=(255,165,0)
    Cy=(0,255,255)

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


    slika=[
        K,K,K,K,K,K,K,K,
        K,K,Y,Y,Y,Y,K,K,
        K,Y,B,Y,Y,B,Y,K,
        K,Y,Y,Y,Y,Y,Y,K,
        K,Y,B,Y,Y,B,Y,K,
        K,Y,Y,B,B,Y,Y,K,
        K,K,Y,Y,Y,Y,K,K,
        K,K,K,K,K,K,K,K,
        ]

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

    temperature=round(sense.get_temperature(), 0)

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

