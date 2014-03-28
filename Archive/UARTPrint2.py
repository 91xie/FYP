import serial
import time
from serial.tools import list_ports

print "UARTReaderStart"

comportname = "/dev/ttyAMA0"
ser = serial.Serial(comportname)

line = ""
try:
    while True:
        data = ser.read()
        if (data=="\r"):
            print(line)
        else:
            line = line + data
except KeyboardInterrupt:
    ser.close()
    pass

#two things are trying to access the port at the same time which could be a problem
#might need to resort to event based programming to read and write.
