numeri = []
<<<<<<< HEAD
for i in range(5):                             #range()  serve per iterare una sequenza di numeri
    num = int(input("Inserire un numero: "))   #attraverso la funzione input() chiedo al utente di inserire dei valori 
    numeri.append(num)                         #che vengono convertiti in intero
print(numeri[5::-1])                           #slicing
#utilizzo lo slicing per stampare il mio array al contrario mettendo prima il range e poi lo step che compio

=======
for i in range(5):
    numeri.append(input("Inserisci un numero:"))
i = len(numeri) - 1
while i >= 0:
    print(numeri[i])
    i = i - 1
>>>>>>> 27831a1718b786f3b14a2f04d35c385f48d64e7b
