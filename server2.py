import threading
import socket

host = "127.0.0.1"
port = 55550

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message.encode('ascii'))

def handle(client):
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message.startswith('NICK'):
                print(f"nickname: {message.split(':')}")
            elif message.startswith('LOGOUT'):
                clients.remove(client)
                break
            print(f"Nova msg: {message}")
            broadcast(message)
        except:
            return exit()


def receive():
    while True:
        client, adress = server.accept()
        print("Conectado a {}".format(str(adress)))
        clients.append(client)

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Servidor tá funcionando")
receive()