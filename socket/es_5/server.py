import sys,socket
def Sort(arr):
    # Converte la stringa in una lista di tuple (nome, cognome, numero)
    contacts = [tuple(line.split()) for line in arr.split('\n') if line.strip()]

    # Ordina la lista di tuple per il nome
    sorted_contacts = sorted(contacts, key=lambda x: x[0])

    # Converte la lista ordinata in una stringa
    sorted_data = '\n'.join([' '.join(contact) for contact in sorted_contacts])

    return sorted_data
                

    
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(("",int(sys.argv[1])))
s.listen(10)

while True :
   print('\nServer in ascolto...')
   soa,addr = s.accept()
   data = soa.recv(1024).decode()
   Sort(data)
   soa.send(data.encode())
   

s.close()
   
   