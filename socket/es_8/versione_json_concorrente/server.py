import sys
import json
import socket
import os

def rimuovi_carattere(json_object):
    return json_object["stringa"].replace(json_object["carattere"], "")

PORT = int(sys.argv[1])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(("", PORT))
s.listen(10)

while True:
    conn, addr = s.accept()
    pid = os.fork()

    if pid == 0:
        s.close()  
        
        print("\nRicevuta connessione da:", addr)
        stringa_json = conn.recv(1024).decode()

        try:
            json_object = json.loads(stringa_json)
            print("\tStringa ricevuta:", json_object["stringa"])
            print("\tCarattere ricevuto:", json_object["carattere"])

            stringa = rimuovi_carattere(json_object)

            conn.send(stringa.encode())
        except json.JSONDecodeError as e:
            print("Errore nella decodifica JSON:", e)

        conn.close()
        sys.exit()  

    else:
        conn.close()  

s.close()