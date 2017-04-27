import conf
from conf import *
import sys
import socket
import _thread
import time

class PiCar:
    def __init__(self):
        self.port = port
        self.sock = socket.socket()
        self.host = socket.gethostname()
        self.sock.bind((self.host,self.port))
        print("Waiting for client...")
        self.sock.listen(1)
        self.clientSock, self.clientAddress = self.sock.accept()#blocks
        print("Client recieved.")
    def checkForData(self):
        recData = clientSock.recv(recVal)#blocks
        print("Got data: ",recData)
        
if __name__ == '__main__':
	piCar = PiCar()
    while True:
        piCar.checkForData()