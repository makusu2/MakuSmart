import sys
import socket
import _thread
import time
import tkinter
from tkinter import *
class Car:
    def __init__(self):
        self.master = Tk()
        self.master.geometry("500x500")
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
        print("Moving forwards")
    def backwards(self):
        print("Moving backwards")
    def turnLeft(self):
        print("Turning left")
    def turnRight(self):
        print("Turning right")
if __name__ == '__main__':
    car = Car()