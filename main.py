import Adafruit_CharLCD as LCD
if __name == "__main__": 
    lcdTest()
def test01():
    GPIO.setmode(GPIO.BCM)#set board mode to Broadcom
    import RPi.GPIO as GPIO
    GPIO.setup(17,GPIO.OUT) #set up pin 17
    GPIO.setup(18,GPIO.OUT)#set up pin 18
    GPIO.output(18,1)#turn on pin 18gr
    GPIO.output(17,1)#turn on pin 17
    print("hi")
def lcdTest():