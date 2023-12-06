import socket
import sys
import os


if len(sys.argv)<5 or not os.path.exists(sys.argv[1]):
    print("Errore negli argomenti  <ip> <porta> <file> <carattere> ")
    exit()
PORT = int(sys.argv[2])             
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[1], PORT))
file = open (sys.argv[3], 'r')
text = file.read()
carattere = sys.argv[4]
s.send(text.encode())
s.recv(1024)
s.send(carattere.encode())
frequenza = s.recv(1024).decode()
print ('Il carattere ', carattere, ' compare ', frequenza, ' volte')
file.close()
s.close()
