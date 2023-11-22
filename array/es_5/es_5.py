import sys
str = ""
for i in range(len(sys.argv)- 1):
    str = sys.argv[1]
    str+=sys.argv[i+1]+" "
print(str)

    

