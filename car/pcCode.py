import sys
import socket
import conf
from conf import *
import time
import _thread
import tkinter
from tkinter import *
class PCGUI:
    def __init__(self):
        self.master = Tk()
        self.master.geometry("500x500")
        
        self.sock = socket.socket()
        hostname, aliaslist, ipaddress = socket.gethostbyaddr(piIP)
        self.host = hostname
        self.port = port
        self.sock.connect((self.host,self.port))
        
        self.forwardButton = Button(self.master,text="Forward",command=self.forward)
        self.backwardsButton = Button(self.master,text="Backwards",command=self.backwards)
        self.turnLeftButton = Button(self.master,text="Turn Left",command=self.turnLeft)
        self.turnRightButton = Button(self.master,text="Turn right",command=self.turnRight)
        self.forwardButton.pack()
        self.backwardsButton.pack()
        self.turnLeftButton.pack()
        self.turnRightButton.pack()
        
        mainloop()
    def forward(self):
        self.sendData(moveNums['F'])
        print("Moving forwards")
    def backwards(self):
        self.sendData(moveNums['B'])
        print("Moving backwards")
    def turnLeft(self):
        self.sendData(moveNums['L'])
        print("Turning left")
    def turnRight(self):
        self.sendData(moveNums['R'])
        print("Turning right")
    def sendData(self,data):
        self.sock.send(data)
    
if __name__ == '__main__':
    pcg = PCGUI()