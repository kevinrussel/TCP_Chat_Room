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
2) The second goald I have right now is to send a message from the server socke to client
3) Okay now te connection is being established properly I need to add in a third connection and see what happens.
4) There is this bug where I need to fix the recieving the messages.
5) Okay so the next change I need to work on is the disconnecting part. 
6) I fixed up the threading, the next thing I need to work on is closing up the port.
7) There are a couple of things I still need to fix, for one we need to have error handling
   additonally, I want to clear up some issues with multi client's joining in.
8) I also want to change up the server such that when a new user joins, all other users will get a message saying " x user has joined!"
9) You know what I want to add? When the user is going to type, their username should already be on the screen. That could be a simple print with no new char.
10) MAJOR BUG, IN A TWO USER SYSTEM, WHEN ONE USER DISCONNECTS CLIENT GOES HAYWIRE.
