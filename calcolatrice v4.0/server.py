import socket, json
from threading import Thread

SERVER_ADDRESS = "127.0.0.1"
SERVER_PORT = 22224
BUFFER_SIZE = 1024

"""_summary_
La funzione avvia_server crea un endpoint di ascolto (sock_listen) dal
quale accettare connesioni in entrata.
La socket di ascolto viene passata alla funzione ricevi_connessioni la
quale accetta le richieste di connessione, per ognuna crea una socket
per i dati (sock_service) che viene passata come parametro ad una
funzione ricevi_comandi eseguita da un thread per servire le richieste
di uno specifico client.
"""

def ricevi_comandi(sock_service, addr_client):
    with sock_service as sock_client:
        while True:
            dati = sock_client.recv(BUFFER_SIZE).decode()
            if not dati:
                break
            msg = json.loads(dati)
            
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

def ricevi_connessioni(sock_listen):
    while True:
        sock_service, addr_client = sock_listen.accept()
        print("\nConnessionie ricevuta da %s" % str(addr_client))
        print("Creo un thread per servire le richieste")
        try:
            Thread(target=ricevi_comandi, args=(sock_service, addr_client)).start()
        except:
            print("Il thread non si avvia")
            sock_listen.close()

def avvia_server(indirizzo, porta):
   
    sock_listen = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_listen.bind((SERVER_ADDRESS, SERVER_PORT))
    sock_listen.listen()
    print(f"Server in ascolto: {indirizzo}:{porta}")
    ricevi_connessioni(sock_listen)
    

if __name__ == "__main__":
    avvia_server(SERVER_ADDRESS, SERVER_PORT)
print("Termina")