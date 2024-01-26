import socket
import json

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_stream:
    socket_stream.connect((SERVER_IP, SERVER_PORT))
    

    while True:
        primoNumero = float(input("Inserisci il primo numero: "))
        operazione = input("Inserire l' operazione (+,-,*,/,%): ")
        secondoNumero = float(input("Inserisci il secondo numero: "))
        
        messaggio = {
            "primoNumero":primoNumero,
            "operazione":operazione,
            "secondoNumero":secondoNumero,
                    }
        messaggio = json.dumps(messaggio)
        socket_stream.send(messaggio.encode("UTF-8"))
        # Riceve il risultato
        data = socket_stream.recv(1024)
        print("Risultato: ",str(data.decode()))
    
    