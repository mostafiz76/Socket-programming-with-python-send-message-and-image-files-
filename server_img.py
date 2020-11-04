
# Server script
# Create server for TCP and IPv4
import socket
import numpy
import cv2
import struct
import pickle

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # ipv4
# Assign an address and a port
server_address = ('server_ip/local',1234)
server.bind(server_address)
# it has to start listening
server.listen()
print("Srever started listening")

frame=cv2.imread('test.jpg')
# Serialize frame
data = pickle.dumps(frame)

while (1000):
	client,client_address = server.accept()
	print("Connected to client")

	# Send message length first
	message_size = struct.pack("L", len(data))
	
	# Then data
	client.sendall(message_size + data)
	print('done sending')
	client.shutdown(socket.SHUT_RDWR)
	client.close()

