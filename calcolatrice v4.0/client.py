import socket, json, sys, random, os, time, threading, multiprocessing

SERVER_IP = "127.0.0.1"
SERVER_PORT = 22224
NUM_WORKERS = 15


    
def genera_richieste(address, port):
    start_time_thread = time.time()
    try:
        s = socket.socket()
        s.connect((address, port))
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_stream:
            socket_stream.connect((SERVER_IP, SERVER_PORT))
            
            scelteOperazione = ['+', '-', '*', '/']
            primoNumero = random.randint(0, 10)
            secondoNumero = random.randint(0,10)
            operazione = random.choice(scelteOperazione)
            messaggio = {
                "primoNumero":primoNumero,
                "operazione":operazione,
                "secondoNumero":secondoNumero,
                        }
            messaggio = json.dumps(messaggio)
            socket_stream.send(messaggio.encode("UTF-8"))
            # Riceve il risultato
            data = socket_stream.recv(1024)
            print(f"Primo numero: {primoNumero} {operazione} {secondoNumero}")
            print("Risultato: ",str(data.decode()))
            print(f"\n{threading.current_thread().name}) Connessione al server: {address}:{port}")
    except:
        print(f"\n{threading.current_thread().name} Qualcosa ha comportato un errore, uscita dal server \n")
        sys.exit()
            
if __name__ == "__main__":
    #avvia_server(SERVER_ADDRESS, SERVER_PORT)
    start_time_thread = time.time()
    threads = [threading.Thread(target=genera_richieste, args=(SERVER_IP, SERVER_PORT)) for _ in range(NUM_WORKERS)]
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]
    end_time_thread = time.time()
    
    print("Tempo totale threads = ", end_time_thread - start_time_thread)
    print("Termina")