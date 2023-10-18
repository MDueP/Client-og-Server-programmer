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
fh = logging.FileHandler('{:%Y-%m-%d}.log'.format(datetime.now()))
format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
fh.setFormatter(format)
logger = logging.getLogger()
logger.addHandler(fh)
logger.setLevel(logging.INFO)

while True:
    message, klient = serverSocket.recvfrom(2048)
    print(message.decode())
    print ()
    logger.info(message.decode())