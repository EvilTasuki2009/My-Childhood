import socket
host = "192.168.1.14"
port = 1720

s = socket.socket()
s.connect((host, port))

str = input("Enter message: ")

while str != "exit":
	s.send(str.encode())

	data = s.recv(1024)
	data = data.decode()
	print("A message from server: " + data)

	str = input("Enter message: ")

s.close
