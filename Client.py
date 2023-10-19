from socket import * #    vi importere her socketen vi anvender for at lave forbindelsen
################################################################################################################################################################
####Variabler vi anvender, før kodens udførelse
serverName = '172.16.0.40' # Serverens IP-addresse - Det skal man vide på forhånd for at forbinde direkte
serverPort = 12000 # hver sikker på at serveren har den samme port. Det er 'nøglen' til døren, så man er sikker på at man går ind af den samme dør, så at sige
clientSocket = socket(AF_INET, SOCK_DGRAM) # her tager vi AddressFamily(IP) og SOCKDGRAM(porten) fra clienten. Vi gemmer de to ting i en variabel for senere brug
#################################################################################################################################################################
####Placeholder print. Det er en indikation til brugere omkring at kode virker og nu er klar. Det er taget fra 
print()
print("======================================")
print("Klienten er klar til at sende beskeder")
print("======================================")
print()
print()
###################################################################
while True:
    message=input('Hvilken spiller?: ') #fortæller brugeren, at den nu skal indtaste hvilken spiller
    clientSocket.sendto(message.encode(), (serverName, serverPort)) #det tidligere input, bliver så sendt til serveren, ved at bruge tidligere allokerede variabler "serverName & serverPort"
#    Med funktionen message.encode laver den også string værdien, som man har indtastet med input funktionen, om til en UTF-8, med andre ord 8-bit. Decoding kommer til at foregå server side
    message=input('Indtast tidspunkt: ')
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    message=input('Indtast hvad du så: ')
    clientSocket.sendto(message.encode(), (serverName, serverPort))
#    Vi gør altså det samme resten af koden, bare med forskellig input, så brugeren ved hvad de skal indtaste
#    vi sender variablen efter hvert input for at vi ikke behøver at lave en variabel for hver input. Den optager altså kun variablen: message. indtil den er sendt til severen og bliver derefter lavet om til det næste input
