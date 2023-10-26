from socket import *

serverName ='172.16.0.40'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

print()
print("==========================")
print("Klar til at sende beskeder")
print("==========================")
print()
print()

while True:
	Hvem = input("Hvad for en spiller: ")
	Hvornår = input("Hvad for et tidspunkt: ")
	Hvad = input("Hvad skete der?: ")
	data = "Klokkeslet: " + Hvornår + "\nHvem: " + Hvem + "\nHvad gjorde de: " + Hvad
	clientSocket.sendto(data.encode(),(serverName, serverPort))	
