# Default TCP and IPv4
# Server socket to accept connections
# Port number range 0 to 65535

import socket

serversocket = socket.socket()
print("Server Socket Created")
serversocket.bind(("localhost", 9999))
serversocket.listen(3)
print("Waiting for client connection requests.")

while True:
    clientsocket, addr = serversocket.accept()
    name = clientsocket.recv(1024).decode()
    #print(clientsocket)
    #print(serversocket)
    print("Client connected with ", addr, name)
    clientsocket.send(bytes("Welcome to Python learning " + name, 'utf-8'))
    clientsocket.close()
