import socket
host = "192.168.1.14"
port = 1720

s = socket.socket()
s.bind((host, port))

s.listen(1)
c, addr = s.accept()
print("A client connected")

while True:
	data = c.recv(1024)
	if not data:
		break
	print("A message from client: " + str(data.decode()))

	data1 = input("Enter message")

	c.send(data1.endcode())

c.close()
