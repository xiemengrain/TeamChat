# TeamChat
An application that supports team chatting 



## Current Features
  - A user can connect to the server and send messages to the peers in the room. 
  - Any messages sent by a user will be broadcasted to any other clients in this chatting room 

## Usage
  - To run the server : python chat_server.py (server configuration is hard coded in the file)
  - To run the client : python chat_client.py hostname port 

## Implementation
#### Critical Modules
  - socket
  - select 
  
  To suppurt non-blocking message forwarding, the server uses the select module from python standard library that will block itself until there is a network activity(e.g a connection request from a client , a message sent from a client , a exceptional connection)
  
  
