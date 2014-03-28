#read from both waspmote and ultrasonic anemometer

import serial
import math
import numpy

ser_ua = serial.Serial("/dev/ttyAMA0",38400)  #Ultrasonic Anemometer
ser_xb = serial.Serial("/dev/ttyUSB0",38400)  #XB module
ser_ws = serial.Serial("/dev/ttyUSB2",115200) #Weather station/waspmote

ser_ua.timeout = 0.1
ser_ws.timeout = 0.1

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
############
##    line = ""
##    while aser.inWaiting():
##        data = aser.read()
##        line = line + data
##    return line
############


def mean_max_min_std(anarray):
    amean = numpy.mean(anarray)
    amax = numpy.max(anarray)
    amin = numpy.min(anarray)
    astd = numpy.std(anarray)
    return [amean, amax, amin, astd]

def float2strarray (afloatarr):
    M = len(afloatarr)
    N = len(afloatarr[0])

    strarr = [[""]*N for _ in range(M)]
    for m in range(M):
        for n in range(N):
            strarr[m][n]= "{0:8.4f}".format(afloatarr[m][n])
            
    return strarr

def stringarray2ser2( Names1D, Str2D, aser):
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

M = 3
N = 100

array2D =[ [0]*N for _ in range(M)]
n = 0

while True:
    if n<N:
        ua_readline = ser_readline(ser_ua)
        if ua_readline != None:
            print ua_readline
            ua_splitline = ua_readline.split(' ')
            ua_splitline = filter(None,ua_splitline)
            for m in range (M):
                array2D[m][n] = float(ua_splitline[m])
            n = n+1
    else:
        ua_outarray = []
        for m in range(M):
            ua_outarray.append(mean_max_min_std(array2D[m]))
        print ua_outarray
        ua_strarray = float2strarray(ua_outarray)
        stringarray2ser2( ["u","v","w"], ua_strarray,ser_xb)
        
        n=0
        #process and sendstringarray2ser2(

    ws_readline = ser_readline(ser_ws)
    if ws_readline!= None:
        print ws_readline
        ser_xb.write(ws_readline+chr(13))
