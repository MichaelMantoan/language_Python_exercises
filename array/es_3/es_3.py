numeri = []

for i in range(10):
    num=int(input("Inserisci un numero: "))
    numeri.append(num)
print("\nnumeri pari\n")
for num in numeri:
    if num % 2 == 0:
        print(num)
print("\nnumeri dispari\n")
for num in numeri:
    if num % 2 != 0:
        print(num)