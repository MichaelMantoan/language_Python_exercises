import sys



def palindroma(stringa):
    for i in range(int(len(stringa) / 2)):
        if stringa[i] != stringa[len(stringa) - 1 - i]:
            return False
    return True


if len(sys.argv) < 2:
    print("argomenti errati")
    exit()

if palindroma(sys.argv[1]):
    print(sys.argv[1] + " è palindroma")
else:
    print(sys.argv[1] + " non è palindroma")

