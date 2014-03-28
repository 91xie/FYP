#built from 14_02_14_UA_XB_WS_1
#combining with datetime checks

from datetime import datetime, date, time, timedelta
import time
import serial
import math
import numpy

ser_ua = serial.Serial("/dev/ttyAMA0",38400)  #Ultrasonic Anemometer
ser_xb = serial.Serial("/dev/ttyUSB2",38400)  #XB module
ser_ws = serial.Serial("/dev/ttyUSB3",115200) #Weather station/waspmote

ser_ua.timeout = 0.01
ser_ws.timeout = 0.01
ser_xb.timeout = 0.01

def ser_readline(aser):
##########
    line = ""
    if aser.inWaiting():
        while True:
            data = aser.read()
            if (data in ("\n\r" + chr(13))):
                return line
            else:
                line = line + data

def mean_max_min_std(anarray):
    amean = numpy.mean(anarray)
    amax = numpy.max(anarray)
    amin = numpy.min(anarray)
    astd = numpy.std(anarray)
    return [amean, amax, amin, astd]

def float2strarray (afloatarr):
    #Converts an array of numbers into a formatted array of strings
    M = len(afloatarr)
    N = len(afloatarr[0])

    strarr = [[""]*N for _ in range(M)]
    for m in range(M):
        for n in range(N):
            #Formatting of the string is done here...
            strarr[m][n]= "{0:8.4f}".format(afloatarr[m][n])
            
    return strarr

def stringarray2serial( Names1D, Str2D, aser):
    print "heklfejfowjefoi"
    
    M = len(Str2D)
    N = len(Str2D[0])
    superline = ""
    for m in range(M):
        line = '%8s'%(Names1D[m])
        for n in range(N):
            line = line + Str2D[m][n]
        superline = superline + line
    print(superline)
    aser.write(superline+chr(13))

ua_M = 4
ws_M = 2

ua_array2D= [[] for _ in range(ua_M)]
ws_array2D= [[] for _ in range(ws_M)]
deltamin= 1
now  = datetime.now()
now_plus_delta = now + timedelta(minutes = deltamin)

while True:
    if datetime.now() < now_plus_delta:
        ua_readline = ser_readline(ser_ua)
        ws_readline = ser_readline(ser_ws)
        if ua_readline != None:
            print ua_readline
            ua_splitline = ua_readline.split(' ')
            ua_splitline = filter(None,ua_splitline)
            for m in range (ua_M):
                ua_array2D[m].append(float(ua_splitline[m]))

##        if ws_readline != None:
##            print ws_readline
##            ws_splitline = ws_readline.split('#')
##            vals = []
##            for apart in ws_splitline:
##                bpart = apart.split(':')[1]
##                vals.append(bpart)
##            #assuming that first val is wind speed in m/s
##            #assuming that secondval is direction
            
        
    else:
        
        ua_outarray = []
        for m in range(ua_M):
            ua_outarray.append(mean_max_min_std(ua_array2D[m]))
        print datetime.now()
        print ua_outarray
        ua_strarray = float2strarray(ua_outarray)
        stringarray2serial( ["u","v","w","t"], ua_strarray,ser_xb)

        #reset buffer
        ua_array2D= [[] for _ in range(ua_M)]
        #reset timer check
        now = now_plus_delta
        now_plus_delta = now + timedelta(minutes = deltamin)

##    ws_readline = ser_readline(ser_ws)
##    if ws_readline!= None:
##        print ws_readline
##        ser_xb.write(ws_readline+chr(13))
    

