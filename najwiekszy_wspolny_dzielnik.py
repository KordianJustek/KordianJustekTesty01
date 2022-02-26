def nwd(a,b):
    while (a!=b):
        if a > b:
            a-=b
        else:
            b-=a
    return a

a = input("Podaj a: ")
b = input("Podaj: ")

print(f"NWD: {nwd(int(a),int(b))}")