#inverti stringhe
import socket
import sys

if len(sys.argv)<2:
    print("Errore negli argomenti <porta>")
    exit()
    
HOST = ""              
PORT = int(sys.argv[1])         
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
while 1:
    print('\nServer in ascolto...')
    conn, addr = s.accept()
    for i in range(0,2):
        str = conn.recv(1024).decode()  
        print ('Stringa ricevuta dal client: ', str)
        str_reverse = str[::-1]
        print ('Stringa reverse: ',str_reverse)
        conn.send(str_reverse.encode())
        
s.close()        