#conta frequenza caratteri
import socket
import sys

def contaFrequenza(string, char):
    frequenza = 0
    for carattere in string:
        if carattere == char:
            frequenza+=1
    return frequenza
    
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
    string = conn.recv(1024).decode()
    conn.send('Stringa ricevuta'.encode())
    print ('Stringa ricevuta dal client: ', string)
    char = (conn.recv(1024).decode())
    print ('Carattere ricevuto dal client: ', char)
    frequenza = contaFrequenza(string, char)
    print ('Frequenza: ',frequenza)
    frequenza_string = str(frequenza)
    conn.send(frequenza_string.encode())
    
s.close()