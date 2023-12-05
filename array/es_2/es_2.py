numeri = []
for i in range(5):
    numeri.append(input("Inserisci un numero:"))
i = len(numeri) - 1
while i >= 0:
    print(numeri[i])
    i = i - 1
