

import socket
import threading



NICKNAME = []
CONNECTION = []

def broad_cast_message (client_socket, message):
    client_socket.sendall(message.encode('utf-8'))
    return




def handle_method(client_socket, message):
    broad_cast_message(client_socket, message)
    while True:
        try:
            message = client_socket.recv(4096)
            if message == b'':
                raise OSError
            message = message.decode("utf-8")
            
            name = ''
            for index,client in enumerate(CONNECTION):
                if (client == client_socket):
                    name = NICKNAME[index]
            if message == "exit":
                print(f"{name} is leaving from server")
                for index, client in enumerate(CONNECTION):
                    if(client != client_socket):
                        broad_cast_message(client,f"{name} has disconnected!")
                    else:
                        broad_cast_message(client, "Goodbye from server")
                CONNECTION.remove(client_socket)
                NICKNAME.remove(name)
                client_socket.close()
                break
            else:
                message = f"{name}: "+ message
                for index, client in enumerate(CONNECTION):
                    if( client!= client_socket ):
                        broad_cast_message(client,message)
        except OSError:
            name = ''
            for index, client in enumerate(CONNECTION):
                if client == client_socket:
                    name = NICKNAME[index]
            CONNECTION.remove(client_socket)
            NICKNAME.remove(name)
            client_socket.close()
            for index, client in enumerate(CONNECTION):
                broad_cast_message(client,f"{name} has lost connection with server")
            

# TODO: Handle in a try catch maybe?
def new_connection_message(client_socket, client_name):

    for index, connections in enumerate(CONNECTION):
        if connections != client_socket:
            message = f"{client_name} has joined the chat!"
            broad_cast_message(connections,message)


## TODO: Handle in a try catch.
def handle_new_connection(client_socket):
            message = "What is your nickname?".encode('utf-8')
            client_socket.sendall(message)
            message = client_socket.recv(4096)
            decoded_message = message.decode("utf-8")
            print(f"The client name is {decoded_message}\n")
            CONNECTION.append(client_socket)
            NICKNAME.append(decoded_message)
            new_connection_message(client_socket,decoded_message)
            return



def connect_method():
    '''
    This method is used to create a connection for new clients.
    '''
    while True:        
        try:
            (client_socket, address) = server.accept()
            handle_new_connection(client_socket)
            thread = threading.Thread(target=handle_method, args=(client_socket,"Hello from Server"))
            thread.start()
        except KeyboardInterrupt:
            break
## Creating a new socket connection.




server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
LOCAL_IP_ADDRESS = '127.0.0.1'
LOCAL_PORT_ADDRESS = 8080
# This will allow the port for reconnection
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCAL_IP_ADDRESS,LOCAL_PORT_ADDRESS))
## How many connections we will support.
server.listen(5)
connect_method()





