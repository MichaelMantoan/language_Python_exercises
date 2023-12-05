numeri = []
numero = int(input("Inserisci numero: "))
while numero != 0:
    numeri.append(numero)
    numero = int(input("Inserisci numero: "))

if len(numeri) % 2 == 0:
    print("Dimensione array pari")
else:
    print("Dimensione array dispari")

