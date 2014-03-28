#built from 14_02_14_UA_XB_WS_4
#going to make a special exception to the rain gauge data
#the array of values need to be summed.


from datetime import datetime, date, time, timedelta
import time
import serial
import math
import numpy

ser_ua = serial.Serial("/dev/ttyAMA0",38400)  #Ultrasonic Anemometer
ser_xb = serial.Serial("/dev/ttyUSB0",38400)  #XB module
ser_ws = serial.Serial("/dev/ttyUSB1",115200) #Weather station/waspmote

ser_ua.timeout = 0.01
ser_ws.timeout = 0.03
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
    if len(anarray)==0:
        print "mean_max_min_std Empty Array"
        return [0]
    
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
            strarr[m][n]= "{0},".format(afloatarr[m][n])
            
    return strarr

def isdigitarray(anarray):
    for aval in anarray:
        try:
            float(aval)
        except ValueError:
            return False
    return True

def stringarray2serial( Names1D, Str2D, aser):
    M = len(Str2D)
    N = len(Str2D[0])
    superline = ""
    for m in range(M):
        line = '%s'%(Names1D[m])
        for n in range(N):
            line = line + Str2D[m][n]
        superline = superline + line
    print superline
    aser.write(superline+chr(13))

def strformat1 (Names1D, Str2D, aser):
    M = len(Str2D)
    N = len(Str2D[0])
    superline = ""
    for m in range(M):
        line = '%s'%(Names1D[m])
        for n in range(N):
            line = line + Str2D[m][n]
        superline = superline + line
    return superline
###########################################################
    #Main
    
ua_M = 4
ws_M = 4

ua_array2D= [[] for _ in range(ua_M)]
ws_array2D= [[] for _ in range(ws_M)]
#ws_array2D= [[]]
deltamin= 0.5
now  = datetime.now()
now_plus_delta = now + timedelta(minutes = deltamin)


ser_readline(ser_ua)
ser_readline(ser_ws)
while True:
    if datetime.now() < now_plus_delta:
        ua_readline = ser_readline(ser_ua)
        ws_readline = ser_readline(ser_ws)
        if ua_readline != None:
            print "ua" + ua_readline
            ua_splitline = ua_readline.split(' ')
            ua_splitline = filter(None,ua_splitline)
            if isdigitarray(ua_splitline) and len(ua_splitline)==ua_M:
                for m in range (ua_M):
                    ua_array2D[m].append(float(ua_splitline[m]))
                
        if ws_readline != None:
            print ws_readline
            if len(ws_readline) >0:
                #print "ws" + ws_readline +">"
                ws_splitline = ws_readline.split('#')
                ws_splitline = filter(None,ws_splitline)
                
                if len(ws_splitline) == ws_M:
                    ws_vals = []
                    for apart in ws_splitline:
                        apart = apart.split(':')
                        apart = filter(None,apart)
                        if apart != None:
                            ws_vals.append(apart[1])
                        
                    if isdigitarray(ws_vals):        
                        for m in range (ws_M):
                            ws_array2D[m].append(float(ws_vals[m]))
                
                #assuming that first val is wind speed in m/s
                #assuming that secondval is direction
            
        
    else:
        
        ua_outarray = []
        ws_outarray1 = [] #this is for mean, max, min, std dev etc.
        ws_outarray2 = [] #this is total, needs one day
        superline = ""
        for m in range(ua_M):
            ua_outarray.append(mean_max_min_std(ua_array2D[m]))
        ua_strarray = float2strarray(ua_outarray)
        superline = superline + strformat1( ["?!ua#u,mean,max,min,std:","#v,mean,max,min,std:","#w,mean,max,min,std:","#t,mean,max,min,std:"], ua_strarray,ser_xb)

        for m in range(ws_M-1): #-1 because we the last value is rain data
            ws_outarray1.append(mean_max_min_std(ws_array2D[m]))
        ws_outarray2.append(numpy.sum(ws_array2D[ws_M-1]))
        
        
        ws_strarray = float2strarray(ws_outarray1)
        superline = superline + strformat1( ["!ws1#u,mean,max,min,std:","#v,mean,max,min,std:","#RH,mean,max,min,std:"], ws_strarray,ser_xb)

        print superline+"!ws2#Rain_mm:"+str(numpy.sum(ws_array2D[ws_M-1]))+chr(13)
        ser_xb.write(superline+"!ws2#Rain_mm:"+str(numpy.sum(ws_array2D[ws_M-1]))+"\n")
        #reset buffer
        ua_array2D= [[] for _ in range(ua_M)]
        ws_array2D= [[] for _ in range(ws_M)]
        #reset timer check
        now = now_plus_delta
        now_plus_delta = now + timedelta(minutes = deltamin)

##    ws_readline = ser_readline(ser_ws)
##    if ws_readline!= None:
##        print ws_readline
##        ser_xb.write(ws_readline+chr(13))
    

