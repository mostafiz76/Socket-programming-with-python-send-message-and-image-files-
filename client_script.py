
# client script

# create a client socket iov4 and TCP.
import socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# connect to server
server_address = ('10.201.1.148',1234)
client.connect(server_address)
# Receive any message
message = client.recv(1000).decode()

# Send the message
client.send("Thanks for connecting".encode())
