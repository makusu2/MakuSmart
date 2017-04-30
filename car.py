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
        
        self.master.bind("<KeyRelease-Up>",self.stopForward)
        self.master.bind("<KeyRelease-Down>",self.stopBackwards)
        self.master.bind("<KeyRelease-Left>",self.stopTurnLeft)
        self.master.bind("<KeyRelease-Right>",self.stopTurnRight)
        
        GPIO.setmode(GPIO.BCM)#set board mode to Broadcom
        for carPin in carPins:
            pinNum = carPins[carPin]
            GPIO.setup(pinNum,GPIO.OUT)
            GPIO.output(pinNum,0)
        GPIO.setup(enablePin,GPIO.OUT)
        GPIO.output(enablePin,1)
        
        mainloop()
    def forward(self,event=None):
        GPIO.output(carPins['F'],1)
    def backwards(self,event=None):
        GPIO.output(carPins['B'],1)
    def turnLeft(self,event=None):
        GPIO.output(carPins['L'],1)
    def turnRight(self,event=None):
        GPIO.output(carPins['R'],1)
    def stopForward(self,event=None):
        GPIO.output(carPins['F'],0)
    def stopBackwards(self,event=None):
        GPIO.output(carPins['B'],0)
    def stopTurnLeft(self,event=None):
        GPIO.output(carPins['L'],0)
    def stopTurnRight(self,event=None):
        GPIO.output(carPins['R'],0)
        
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