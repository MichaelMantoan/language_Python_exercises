import sys





if len(sys.argv) < 2:
    print("argomenti errati")
    exit()

concatenata = ""
for i in range(1, len(sys.argv)):
    concatenata += sys.argv[i] + " "
print(concatenata)

