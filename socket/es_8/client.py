import socket
import sys

if len(sys.argv) < 4 or not os.path.exists(sys.argv[1]):
    print("Errore negli argomenti<indirizzo ip> <porta> <stringa> <carattere> ")
    exit()

PORT = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[1], PORT))

s.send(sys.argv[3].encode())
s.recv(10)
s.send(sys.argv[4].encode())

stringa = s.recv(len(sys.argv[3])).decode()

print("Stringa %s senza carattere: %c " % (stringa, sys.argv[4]))

s.close
