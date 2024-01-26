import socket, json
from threading import Thread

SERVER_ADDRESS = "127.0.0.1"
SERVER_PORT = 22224

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
    sock_service.close()

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
    
    ricevi_connessioni(sock_listen)

if __name__ == "__main__":
    avvia_server(SERVER_ADDRESS, SERVER_PORT)
print("Termina")