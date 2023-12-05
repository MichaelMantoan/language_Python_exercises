
numeri = []
numero = int(input("Inserisci numero: "))
while numero != 0:
    numeri.append(numero)
    numero = int(input("Inserisci numero: "))


somma = 0
for numero in numeri:
    somma += numero

media = somma / len(numeri)
print("media: ", media)


print("Numeri maggiori della media: ")
reverse = numeri[::-1]
for numero in reverse:
    if numero >= media:
        print(numero)

