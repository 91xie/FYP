"""
CONSULT https://sites.google.com/site/semilleroadt/raspberry-pi-tutorials/gpio
I reckon that you need to go to event based programming to figure out how to
simulatenously read and write at the same time. Consider GUI and event based
programming.

CONSIDER using Glade, look up "Using Glade to create GUI's - PiText"
You might want to bring your PI home and install it via Ethernet cable.
Or you could get a port sorted out in your lab.
"""
import serial
import time


print "UARTReaderRead"
astring = "Hello Waspmote, from Raspberry Pi\n"


ser = serial.Serial("/dev/ttyAMA0",115200)
ser.write(astring)
ser.close()

