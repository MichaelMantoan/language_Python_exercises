<<<<<<< HEAD
import sys
import json
import socket
import os
=======
import sys, json, socket, os

>>>>>>> 8e63ec8666803bc35ac95c5df5e7d4658dcfe90d

def rimuovi_carattere(json_object):
    return json_object["stringa"].replace(json_object["carattere"], "")

<<<<<<< HEAD
=======

>>>>>>> 8e63ec8666803bc35ac95c5df5e7d4658dcfe90d
PORT = int(sys.argv[1])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(("", PORT))
s.listen(10)

<<<<<<< HEAD
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
=======
while 1:
    conn, addr = s.accept()
    print("\nRicevuta connessione da: ", addr)

    if os.fork() == 0:
        s.close()

        stringa_json = conn.recv(1024).decode()

        json_object = json.loads(stringa_json)

        print("\tStringa ricevuta: " + json_object["stringa"])
        print("\tCarattere ricevuto: " + json_object["carattere"])

        stringa = rimuovi_carattere(json_object)

        conn.send(stringa.encode())
        conn.close()
        sys.exit(0)

    conn.close()

s.close()
>>>>>>> 8e63ec8666803bc35ac95c5df5e7d4658dcfe90d
