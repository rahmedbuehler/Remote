import socket

socket = socket.socket()

port = 100000
socket.connet(('127.0.0.1', port))
print(socket.recv(1024))
socket.close()