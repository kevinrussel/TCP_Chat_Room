import threading
import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1',8080))
write = True
def write_message():
    while write:
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

    return
    

def create_connection():
    message = threading.Thread(target=write_message, args=())
    message.start()
    recieve_message()
    return



if __name__ == '__main__':
    create_connection()