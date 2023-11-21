numeri = []
for i in range(5):                             #range()  serve per iterare una sequenza di numeri
    num = int(input("Inserire un numero: "))   #attraverso la funzione input() chiedo al utente di inserire dei valori 
    numeri.append(num)                         #che vengono convertiti in intero
print(numeri[5::-1])                           #slicing
#utilizzo lo slicing per stampare il mio array al contrario mettendo prima il range e poi lo step che compio

