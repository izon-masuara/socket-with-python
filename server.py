import threading
import socket

host = "127.0.0.1"
port = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((host, port))
server.listen()

clients = []

def handle(client):
    while True:
        message = client.recv(1024)
        for client in clients:
            client.send(message)

def recieve():
    while True:
        client, address = server.accept()
        print(address)
        clients.append(client)
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server running")
recieve()