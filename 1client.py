import socket
import threading
import os

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1',5555))

chat = f''''''

def recieve():
    global chat
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message[len(message) - 1] == "1":
                message = message[:-1]
                chat += f'''>>>>  {message} \t\t\n'''
            else :
                message = message[:-1]
                chat += f'''\t\t{message}  <<<<<\n'''
            os.system('clear')
            print(chat)
        except:
            print('Error Occured while Connecting')
            client.close()
            break
        
def write():
    while True:
        message = input("") + "1"
        client.send(message.encode('ascii'))

recieve_thread = threading.Thread(target=recieve)
recieve_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()