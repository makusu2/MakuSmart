import sys
import socket
import _thread
import time
import tkinter
from tkinter import *
import carConf
from carConf import *
import RPi.GPIO as GPIO
class Car:
    def __init__(self):
        self.master = Tk()
        self.master.geometry("500x500")
        self.forwardButton = Button(self.master,text="Forward",command=self.forward)
        self.backwardsButton = Button(self.master,text="Backwards",command=self.backwards)
        self.turnLeftButton = Button(self.master,text="Turn Left",command=self.turnLeft)
        self.turnRightButton = Button(self.master,text="Turn right",command=self.turnRight)
        self.stopButton = Button(self.master,text="Stop",command=self.stop)
        self.forwardButton.pack()
        self.backwardsButton.pack()
        self.turnLeftButton.pack()
        self.turnRightButton.pack()
        self.stopButton.pack()
        
        self.master.bind("<Left>",self.turnLeft)
        self.master.bind("<Right>",self.turnRight)
        self.master.bind("<Up>",self.forward)
        self.master.bind("<Down>",self.backwards)
        self.master.bind("<Return>",self.stop)
        
        GPIO.setmode(GPIO.BCM)#set board mode to Broadcom
        for carPin in carPins:
            pinNum = carPins[carPin]
            GPIO.setup(pinNum,GPIO.OUT)
            GPIO.output(pinNum,0)
        GPIO.setup(enablePin,GPIO.OUT)
        GPIO.output(enablePin,1)
        
        mainloop()
    def forward(self):
        print("Moving forwards")
        self.changePin(pin=carPins['F'])
    def backwards(self):
        print("Moving backwards")
        self.changePin(pin=carPins['B'])
    def turnLeft(self):
        print("Turning left")
        self.changePin(pin=carPins['L'])
    def turnRight(self):
        print("Turning right")
        self.changePin(pin=carPins['R'])
    def stop(self):
        print("Stopping")
        self.clearPins()
    def clearPins(self):
        for carPin in carPins:
            pinNum = carPins[carPin]
            GPIO.output(pinNum,0)
    def changePin(self,pin=None):
        if pin==None:
            self.clearPins()
        else:
            for carPin in carPins:
                pinNum = carPins[carPin]
                if (pin == carPin) or (pin == pinNum):
                    GPIO.output(pinNum,1)
                else:
                    GPIO.output(pinNum,0)
if __name__ == '__main__':
    car = Car()