#Encrypted Chatroom Asymetric method

import socket
import threading


choice = input("Do you want to be a Host or Connect? (h/c): ")
if choice == "h":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Indicates that server is using IPV4 and TCP protocol
    server.bind(("127.0.0.1", 9999)) # defines IP and Port for the Server
    server.listen(10)
    
    client, _ = server.accept()
    
elif choice == "c": 
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 9999))

else: 
    exit()
    

def send_messages(c):
    while True:
        message = input("")
        c.send(message.encode())
        print("You: " + message)
        if message == "/exit":
            exit()
        
def receive_message(c):
    while True:
        print("User: " + c.recv(1024).decode())

threading.Thread(target=send_messages, args=(client,)).start()
threading.Thread(target=receive_message, args=(client,)).start()


    
    
