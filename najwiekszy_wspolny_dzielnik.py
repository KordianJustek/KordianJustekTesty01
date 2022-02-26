def nwd(a,b):
    while (a!=b):
        if a > b:
            a-=b
        else:
            b-=a
    return a

a = int(input("Podaj a: "))
b = int(input("Podaj:b "))

print(f"Najwiekszy Wspolny Dzielnik: {nwd(int(a),int(b))}")
print(f'Najmniejsza Wspolna Wielokrotnosc: {int((a*b)/nwd(a,b))} ')
