### This is a simple TCP chatroom with a bit of functionaility that we are doing.


#### Main goals of this project
- This project is for a couple reasons. We are learning how to use threading, and sockets. How to connect to a server, as well how to handle connections.

## Server Class

- This will be the server which will handle ther connections and forward the messages to the other client.
- As well as handling client's disconnecting. 

#### Server Class Methods
Import threading and import socket

**Broadcast Method**
- This method sends a method to all connections.

**Handle Method**
- Sends message to broadcast method
- If this fails, close the connection
- Tells others connections that the user left.

**Receive Method**
- Receieve client connection
- Tells other users that the client is connected.


