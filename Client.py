from socket import *

serverName = '172.16.0.40'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

print()
print("==========================")
print("Klar til at sende beskeder")
print("==========================")
print()
print()

while True:
    message=input('Skriv noget til serveren: ')
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    message=input('Indtast tidspunkt: ')
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    message=input('Indtast hvad du så: ')
    clientSocket.sendto(message.encode(), (serverName, serverPort))