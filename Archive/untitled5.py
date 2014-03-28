import serial
from serial.tools import list_ports

for acomp in list_ports.comports():
    print acomp[0]
