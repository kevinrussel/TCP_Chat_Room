import threading
import socket

# We are going to be making a client right now for our server

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1',8080))
message = client.recv(4096)
print(f"message recieved{message.decode("utf-8")}")
