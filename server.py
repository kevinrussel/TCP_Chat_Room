

import socket
import threading



NICKNAME = []
CONNETION = []
def handle_method(client_socket, message):
    print("hitting")
    client_socket.sendall(message.encode('utf-8'))
    pass


def connect_method():
    '''
    This method is used to create a connection for new clients.
    '''
    while True:
        (client_socket, address) = server.accept()
        print("I have recieved the conneciton")
        print(f'The client socket_connection is {client_socket} and the address is {address}')
        thread = threading.Thread(target=handle_method, args=(client_socket,"Hello from Server"))
        thread.start()
## Creating a new socket connection.




server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
LOCAL_IP_ADDRESS = '127.0.0.1'
LOCAL_PORT_ADDRESS = 8080
server.bind((LOCAL_IP_ADDRESS,LOCAL_PORT_ADDRESS))
## How many connections we will support.
server.listen(5)
connect_method()





