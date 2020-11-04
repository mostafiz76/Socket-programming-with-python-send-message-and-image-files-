# Server script
# Create server for TCP and IPv4
import socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # ipv4
# Assign an address and a port
server_address = ('10.201.1.148',1234)
server.bind(server_address)
# it has to start listening
server.listen()
print("Srever started listening")
# if there is any connection it has to accept
while True:
    client,client_address = server.accept()## establishing connection with the client
    print("Connected to client")
    # Greet message
    client.send("Hey!, Welcome".encode())
    print(client_address)
    print(client.recv(1000).decode())
    


