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
    spiller=input('Skriv noget til serveren: ')
    tidspunkt=input('Indtast tidspunkt: ')
    observation=input('Indtast hvad du så: ')
    message=(spiller, tidspunkt, observation)
    clientSocket.sendto(message.encode(), (serverName, serverPort))