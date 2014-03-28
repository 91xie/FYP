#send basic string to xbee

import serial

ser_xb = serial.Serial("/dev/ttyUSB0",38400)
print "hello"
while True:
    aline = raw_input("Write here:")
    ser_xb.write(aline+"\n")
