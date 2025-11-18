import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5555))

def receive():
    while True:
        print(client.recv(1024).decode())

threading.Thread(target=receive).start()

while True:
    msg = input()
    client.send(msg.encode())