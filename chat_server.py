# server is handling the sockets in non-blocking mode using
import sys
import socket
import select


SERVER_ADDRESS = ('localhost', 8888)
DATA_BLOCK = 1024
inputs = []
outputs = []


# create a server that listens to connection and message fron clients
def start_server():


    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(SERVER_ADDRESS)
    server_socket.listen(10)
    print("Listening to port [%s ,%s]" % SERVER_ADDRESS)
    inputs.append(server_socket)
    while inputs:
        readable_sockets , writable_sockets, exceptional_sockets = select.select(inputs,outputs,inputs)

        for readable_socket in readable_sockets:
            # Add new connection to readable_socket socket
            if readable_socket is server_socket :
                new_connection, addr = server_socket.accept()
                print >> sys.stderr, "A new connection from [%s,%s]" % addr
                inputs.append(new_connection)
            # Add the message from the socket to the message queue of that socket
            else:
                data = readable_socket.recv(DATA_BLOCK)
                print >> sys.stderr, "A new message from [%s ,%s] " % addr
                print >> sys.stderr, "message is %s" % data
                if data:
                    broadcast(server_socket,readable_socket,data)
                else:
                    inputs.remove(readable_socket)
                    # Broadcast that one client the offline
                    broadcast(server_socket,readable_socket, "Client (%s , %s) is offline \n" % addr)

def broadcast(server_socket, readable_socket, msg):
    for socket in inputs :
        if socket is not server_socket and socket is not readable_socket:
            try:
                print >> sys.stderr, "send message from [%s ,%s] to peers" % socket.getpeername()
                addr = socket.getpeername()
                socket.send("Message from %s : %s " % (addr,msg))
            except:
                socket.close()
                # Broadcast that one client the offline


if __name__ == "__main__":
    start_server()