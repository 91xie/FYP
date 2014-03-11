from datetime import datetime, date, time, timedelta
import time
import serial
import math
import numpy

ser_xb = serial.Serial("/dev/ttyUSB0", 38400) #xb module

ser_xb.flush()

while True:
    print "write"
    ser_xb.write(str(datetime.now())+":hello\n")
    time.sleep(5)
