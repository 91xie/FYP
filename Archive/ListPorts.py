import os
import serial
from serial.tools import list_ports

def list_serial_ports():
    #windows
    if os.name == 'nt':
        #scan for available ports
        available = []
        for i in range (256):
            try:
                s=serial.Serial(i)
                available.append('COM'+str(i+1))
                s.close()
            except serial.SerialException:
                pass
            return available

        else:
            #mac/linux
            return [port[0] for port in list_ports.comports()]

for port in list_ports.comports():
    print(port[0])

