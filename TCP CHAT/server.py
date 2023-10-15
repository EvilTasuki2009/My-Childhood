import threading
import socket

# Connection Data
host = '127.0.0.1'
port = 55555

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# Lists For Clients and Their Nicknames
clients = []
nicknames = []

# Sending Messages To All Connected Clients
def broadcast(message):
    for client in clients:
        client.send(message)

# Handling Messages From Clients
def handle(client):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            if msg.decode('ascii').startswith('KICK'):
                name_to_kick = msg.decode('ascii')[5:]
                kick_user(name_to_ban)
            elif msg.decode('ascii').startswith('BAN'):
                name_to_ban = msg.decode('ascii')[4:]
                ban_user(name_to_ban)
                with open('bans.txt', 'a') as f:
                    f.write(f'{name_to_ban}\n')
                print(f'{name_to_ban} was banned')
            else:
                broadcast(message)
        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break


# Receiving / Listening Function
def receive():
    while True:
        # Accept Connection
        client, address = server.accept()
        print("Connected with ".format(str(address)))

        # Request And Store Nickname
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')


        if nickname == 'Adminloc':
        	client.send("PASSWORD FOR THE ACCOUNT: ".encode('ascii'))
        	password = client.recv(1024).decode('ascii')

        	if password != "25/06/2009":
        		client.send("REFUSED".encode('ascii'))
        		client.close()
        		continue



        nicknames.append(nickname)
        clients.append(client)

        # Print And Broadcast Nickname
        print("Nickname is {}".format(nickname))
        broadcast("{} joined the chat!".format(nickname).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))

        # Start Handling Thread For Client
        thread = threading.Thread(target = handle, args = (client, ))
        thread.start()

def kick_user(name):
	if name in nicknames:
		name_index = nicknames.index(name)
		client_to_kick = clients[name_index]
		clients.remove(client_to_kick)
		client_to_kick.send('You were kick by Adminloc'.encode('ascii'))
		client_to_kick.close()
		nicknames.remove(name)
		broadcast(f'{name} was kicked by Adminloc')

print('Server started and ready to connect!'.encode('ascii'))
receive()
