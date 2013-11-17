#This function could be used to list all of the ports python
#python -m serial.tools.list_ports
#found code from www.atlas-scientific.com/_files/code/pi_sample_code.pdf
#allows you to list comports

import serial
import time
from serial.tools import list_ports

savetofile = False

print("Port are as follows")
for i in range(0,len(list_ports.comports())):
    print( str(i) + ": " + list_ports.comports()[i][0])

#select the comport number
comindex = input('Type in COM Port Index: ')
comportname = list_ports.comports()[comindex][0]
baudrate = input('Type in Baud Rate: ')
ser = serial.Serial(comportname,baudrate)



print('Start')
line = ""

while True:
    data = ser.read()
    if (data=="\r"):
        print(line)
        if savetofile == True:
            f = open('/home/pi/Desktop/data.txt','a')
            f.write(line)
            f.close()#there could be a problem closing the file
            #need to figure out a way of closing it at the very end.
    else:
        line = line + data

