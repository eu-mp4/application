import threading
import socket

nickname = input("Escolha um nick: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 55555))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("Ocorreu um erro")
            client.close()
            break

def write():
    while True:
        message = input(f'{nickname}: ')
        #message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()
while True:
    message = input(f'{nickname}: ')
    #message = '{}: {}'.format(nickname, input(''))
    client.send(message.encode('ascii'))
#write_thread = threading.Thread(target=write)
#write_thread.start()
