import socket
import sys

PORT = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[1], PORT))

s.send(sys.argv[3].encode())
s.recv(10)
s.send(sys.argv[4].encode())

stringa = s.recv(len(sys.argv[3])).decode()

print("Stringa %s senza carattere: %c " % (stringa, sys.argv[4]))

s.close
