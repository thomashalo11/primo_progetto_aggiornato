import socket
import json

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_server:
    sock_server.bind((SERVER_IP, SERVER_PORT))
    sock_server.listen()
    print(f"Server in ascolto su: {SERVER_IP}:{SERVER_PORT}")
    
    
    msg = ""

    while True:
        sock_service, address = sock_server.accept()
        print(f"Connessione stabilita: - {address[0]}:{address[1]}")
        with sock_service as sock_client:
            while True:
                # msg = data.decode()
                dati = sock_client.recv(BUFFER_SIZE).decode()
                if not dati:
                    break
                msg = json.loads(dati)


                # Se l' input è "Esci", viene conclusa la connessione
                if msg == "Esci":
                    print("Connessione conclusa")
                    break
                
                risultato = 0

                print("Lista: ", msg)
                operando1 = msg["primoNumero"]
                operazione = msg["operazione"]
                operando2 = msg["secondoNumero"]

                print(operando1)
                print(operazione)
                print(operando2)

                # Trasformiamo le stringhe in int
                num1 = int(operando1)
                num2 = int(operando2)

                if operazione == "+":
                    risultato = num1 + num2
                elif operazione == "-":
                    risultato = num1 - num2
                elif operazione == "/":
                    risultato = num1 / num2
                elif operazione == "*":
                    risultato = num1 * num2

                output = str(risultato)
                output = json.dumps(output)
                output = output.encode()

                sock_client.send(output)