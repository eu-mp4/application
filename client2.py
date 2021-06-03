import threading
import socket

nickname = input("Escolha um nick: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 55550))


def receive():
    while True:
        message = client.recv(1024).decode('ascii')
        print(message)

def write():
    while True:
        message = input(f'{nickname}: ')
        client.send(message.encode('ascii'))
        print(message)

receive_thread = threading.Thread(target=receive)
receive_thread.start()

client.send(f'NICK:{nickname}'.encode('ascii'))
while True:
    print('{}'.format(nickname), end=": ")
    message = input()
    client.send(message.encode('ascii'))


    