from socket import *
import logging
from datetime import datetime

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)

print()
print("===============================")
print("Serveren er klar til at modtage")
print("===============================")
print()
print()
tid = logging.FileHandler('{:%Y-%m-%d}.log'.format(datetime.now()))

while True:
    message, klient = serverSocket.recvfrom(2048)
    format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    tid.setFormatter(format)
    logger = logging.getLogger()
    logger.addHandler(tid)
    logger.setLevel(logging.INFO)
    print(message.decode())
    print(klient)
    print ()
    log = message.decode(), str(klient)
    logger.info(log)