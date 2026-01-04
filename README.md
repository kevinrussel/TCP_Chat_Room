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


## Client Method

Import Threading and Socket

***Hint***: We shoiuld have two threads taking place, one that is the recieve and one that is write.

### Recieve method:
- Recieve the message from the server
- Close connection if there is an error

### Write method:
- It should send a write command.



How I am going about this:
1) The first things I need to do is to figure out how to connect to my server via a client.