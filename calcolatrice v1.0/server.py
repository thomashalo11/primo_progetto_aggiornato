import socket
import json

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, SERVER_PORT))


msg = ""

while True:
    data, addr = sock.recvfrom(BUFFER_SIZE)
    msg = data.decode()
    msg = json.loads(data)
    
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
    
    
    sock.sendto(output, addr)
sock.close()