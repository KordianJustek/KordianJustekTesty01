import sys
from random import randint

def losowanie():
    tablica = []
    i = 1
    while i <= 6:
        wylosowana_liczba = randint(1,49)
        while wylosowana_liczba in tablica:
            wylosowana_liczba = randint(1, 49)
        else:
            tablica.append(wylosowana_liczba)
        i+= 1
    return tablica

def sprawdz(maszyna,czlowiek):
    i,j =0,0
    wygrane = 0
    #maszyna = [ 17,27,44,46,9,1]
    #czlowiek =[17,43,44,41,12,35]
    while i < 6:
        while j < 6:
            if czlowiek[i]==maszyna[j]:
                sys.stdout.write(f"{czlowiek[i]} ")
                wygrane +=1
            j+=1
        i+=1
        j=0
    return wygrane

z = 0

tablica_wygrane = [0,0,0,0,0,0,0]

while z < 48000000:
    maszyna = losowanie()
    czlowiek = losowanie()
    print(f'Maszyna losujaca: {maszyna}' )
    print(f'Liczby Gracza   : {czlowiek} ' )
    wygrane = sprawdz(czlowiek,maszyna)
    print(f'\nTrafiono : {wygrane} liczby ')
    z+=1
    a=0
    while a < 7:
        if wygrane == a:
            tablica_wygrane[a] =tablica_wygrane[a] + 1
        a+=1

x = print(f"trafiono: {tablica_wygrane}")
