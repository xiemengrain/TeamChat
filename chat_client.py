import sys
import socket

import select

inputs = [sys.stdin]
outputs = []
DATA_BLOCK = 1024
def start_client():

    if (len(sys.argv) < 3):
        print('Usage : python chat_client.py hostname port')
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.settimeout(2)

    # connect to remote host
    try :
        client_socket.connect((host, port))
    except :
        print('Unable to connect')
        sys.exit()

    inputs.append(client_socket)
    print ('Connected to remote host. You can start sending messages')
    sys.stdout.write('[ME]: ')
    sys.stdout.flush()

    while True:
        readable_sockets, writable_sockets, exceptional_sockets = select.select(inputs, outputs, [])

        for readable_socket in readable_sockets:
            if readable_socket is client_socket:
                data = readable_socket.recv(DATA_BLOCK)
                if not data:
                    print >> sys.stderr , "No Connection from server"
                    sys.exit()
                else:
                    print("\n"+data)
                    sys.stdout.write('[ME]: ')
                    sys.stdout.flush()
            else:
                client_socket.send(sys.stdin.readline())
                sys.stdout.write('[ME]: ')
                sys.stdout.flush()

if __name__ == "__main__":

    sys.exit(start_client())