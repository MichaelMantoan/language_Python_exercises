numeri = []

while True:
    num = int(input("Inserisci un numero > 0 (termina la serie con 0): "))
    
    
    if(num == 0):
        if(len(numeri) % 2 == 0):
            print("Pari")
        else:
            print("Dispari")
        break

    if(num > 0):
        numeri.append(num)
    else:
        break

    