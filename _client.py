#!/usr/bin/env python
# coding: utf-8

# In[1]:


from socket import *

server_address = ("127.0.0.1", 53535)
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(server_address)

n = 0

while True:
    n = int(input("Enter a number between 1 to 100: "))
    if n >= 1 and n <= 100:
        break
    else:
        print("Invalid input! Please enter a number between 1 to 100.")

name = input("Enter your name: ")
message = name + "," + str(n)

client_socket.send(message.encode())

response = client_socket.recv(2048).decode().strip().split(",")
print("Server Name: "+ response[0])
print("Server generated number: " + response[1])

client_socket.close()

