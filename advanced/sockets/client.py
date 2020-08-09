import socket


clientsocket = socket.socket()
print("Client Socket Created")

clientsocket.connect(("localhost", 9999))

name = input("Enter your name: ")
clientsocket.send(bytes(name, 'utf-8'))

print(clientsocket.recv(1024).decode())