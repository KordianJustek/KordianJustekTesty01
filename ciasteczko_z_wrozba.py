from random import randint

def rzucam():
    o = 0
    r = 0
    i = 0
    while i < 100:
        rzut = randint(0,1)
        if rzut == 0:
            o += 1
        if rzut == 1:
            r += 1
        i+=1
    print("Rzucałem 100 razy moneta")
    print(f"Orzeł wypadł: {o} Reszka wypadła: {r}")

rzucam()
