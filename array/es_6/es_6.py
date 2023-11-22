import sys

def palindroma(str):
    c = str[len(str)::-1]
    if (c == str):
        return 1
    else:
        return -1

str = sys.argv[1]
if palindroma(str) == 1:
    print("\nè palindroma\n")
else:
    print("\nnon è palindroma\n")