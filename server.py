import threading
import socket

host = "127.0.0.1"
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            print(message)
            broadcast(message)
        except:
            print('fosnfso')
        #    index = clients.index(clients)
        #    clients.remove(client)
        #    client.close()
        #    nickname = nicknames[index]
        #    broadcast("{} deixou o chat".format(nickname).encode('ascii'))
        #    nicknames.remove(nickname)
        #    break

def receive():
    while True:
        client, adress = server.accept()
        print("Conectado a {}".format(str(adress)))

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)
        print(clients)
        print("Nickname do cliente é {}".format(nickname))
        broadcast("{} entrou no chat".format(nickname).encode('ascii'))
        client.send("Conectado ao servidor!".encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))

print("Servidor tá funcionando")
receive()