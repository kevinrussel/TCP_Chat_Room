import threading
import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1',8080))


def write_message():
    print("in here")
    while True:
        message = input()
        message = message.encode('utf-8')
        client.sendall(message)



# We are going to be making a client right now for our server
def recieve_message():
    print("We are in the recieve message")
    while True:
        message = client.recv(4096)
        print(len(message))
        print(f"mnessage recieved {message.decode("utf-8")}")


def create_connection():
    message = threading.Thread(target=recieve_message, args=())
    message.start()
    write_message()




if __name__ == '__main__':
    create_connection()