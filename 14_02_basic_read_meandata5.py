import serial
import math
import numpy

##serial begin
ser = serial.Serial("/dev/ttyAMA0",38400)
ser2 = serial.Serial("/dev/ttyUSB0",38400)
serWS = serial.Serial("/dev/ttyUSB2",115200)
def ser_readline():
    line = ""
    while True:
        data = ser.read()
        if (data != chr(13)):
            line = line + data
        else:
            return line

def ser2_readline():
    line = ""
    while True:
        data = ser2.read()
        if (data != chr(13)):
            line = line + data
        else:
            return line

def serWS_readline():
    bline = ""
    while True:
        data = serWS.read()
        if (data!=chr(13)):
            bline = bline + data
        else:
            return bline

def float2strarray (afloatarr):
    M = len(afloatarr)
    N = len(afloatarr[0])

    strarr = [[""]*N for _ in range(M)]
    for m in range(M):
        for n in range(N):
            strarr[m][n]= "{0:8.4f}".format(afloatarr[m][n])
            
    return strarr

def stringarray2ser2( Names1D, Str2D):
    M = len(Str2D)
    N = len(Str2D[0])
    superline =""
    for m in range(M):
        line = '%8s'%(Names1D[m])
        for n in range(N):
            line = line + Str2D[m][n]
        superline = superline + line
        #ser2.write(line+chr(13))
    ser2.write(superline+chr(13))
        

def mean_max_min_std(anarray):
    amean = numpy.mean(anarray)
    amax = numpy.max(anarray)
    amin = numpy.min(anarray)
    astd = numpy.std(anarray)
    return [amean, amax, amin, astd]

####################################

splitline = ser_readline().split(' ')
splitline = filter(None, splitline) 

M = len(splitline)
N = 100
array2D =[ [0]*N for _ in range(M)]

n = 0

while True:
    
    if n<N:
        areadline = ser_readline()
        print areadline
        splitline = areadline.split(' ')
        splitline = filter(None, splitline)

        for m in range(M):
            array2D[m][n]=float(splitline[m])
        n=n+1
    else:
        WSread = serWS_readline()
        ser2.write(WSread + chr(13))
        #don't read as the array is full.
        outarray = []
        for m in range(M):
            outarray.append(mean_max_min_std(array2D[m]))
        print outarray
        strarray = float2strarray(outarray)
        stringarray2ser2( ["u","v","w"], strarray)
        
        n=0
        #process and send
