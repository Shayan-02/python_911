import socket
import threading

clients = []

def handle_client(conn, addr):
    while True:
        try:
            msg = conn.recv(1024).decode()
            broadcast(f"{addr}: {msg}")
        except:
            clients.remove(conn)
            conn.close()
            break

def broadcast(msg):
    for c in clients:
        c.send(msg.encode())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5555))
server.listen()
print("Chat server running...")

while True:
    conn, addr = server.accept()
    clients.append(conn)
    threading.Thread(target=handle_client, args=(conn, addr)).start()