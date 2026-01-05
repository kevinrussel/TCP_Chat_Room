

import socket
import threading



NICKNAME = []
CONNECTION = []

def broad_cast_message (client_socket, message):
    client_socket.sendall(message.encode('utf-8'))
    return


def handle_method(client_socket, message):
    broad_cast_message(client_socket, message)
    print("about to hit the true")
    while True:
        message = client_socket.recv(4096)
        message = message.decode("utf-8")
        broad_cast_message(client_socket,message)


def connect_method():
    '''
    This method is used to create a connection for new clients.
    '''
    while True:
        
        try:
            (client_socket, address) = server.accept()
            print(f'The client socket_connection is {client_socket} and the address is {address}')
            message = "What is your nickname".encode('utf-8')
            client_socket.sendall(message)
            message = client_socket.recv(4096)
            message = message.decode("utf-8")
            print("The client name is {message}")
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





