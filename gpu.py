#GPIO GUI
import tkinter
from tkinter import *
from PIL import ImageTk, Image
import os
class Gpu:
    def __init__(self,master=Tk()):
        self.master = master
        gpioImage = Image.open("pinout.png")
        gpioImage.load()
        gpioPhotoImage = ImageTk.PhotoImage(gpioImage)
        gpioPanel = Label(master,image=gpioPhotoImage)
        gpioPanel.pack(side="bottom",fill="both",expand="yes")
        master.mainloop()
gpu = Gpu()