def Media(numeri):
    media = sum(numeri) / len(numeri)
    return media

numeri = []

while True:
    num = int(input("Inserisci un numero > 0 (termina la serie con 0): "))
    
    if(num > 0):
        numeri.append(num)
    else:
        break
m = Media(numeri)
print("Media dei numeri: ",m)
print("\nvalori superiori alla media visualizzati all'inverso:\n")
tmp = numeri[::-1]
for i in range(len(numeri)):
    if tmp[i] > m:
        print(tmp[i])
