import threading
import socket
import threading
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1',8080))

def write_message():
    while True:            
        message = input()
        message = message.encode('utf-8')
        client.sendall(message)



# We are going to be making a client right now for our server
def recieve_message():
    
    while True:
        message = client.recv(4096) 
        message = message.decode('utf-8')
        print(f"{message}")
        if message == "Goodbye from server":
            break
        elif len(message) == 0:
            print("DISCONNECTED FROM SERVER")
            break
    return
    

def create_connection():
    message = threading.Thread(target=write_message, args=(), daemon=True)
    message.start()
    recieve = threading.Thread(target=recieve_message, args=())
    recieve.start()
    recieve.join()
    return
    



if __name__ == '__main__':
    create_connection()
    