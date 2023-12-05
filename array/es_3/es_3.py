numeri = []

for i in range(10):
    numeri.append(int(input("Inserisci un numero: ")))
pari = []
dispari = []
for numero in numeri:
    if numero % 2 == 0:
        pari.append(numero)
    else:
        dispari.append(numero)
print("numeri pari: ", pari)
print("numeri dispari: ", dispari)


