import serial
serxbee = serial.Serial("/dev/ttyUSB0",38400)
serua = serial.Serial("/dev/ttyAMA0",38400)
serws = serial.Serial("/dev/ttyUSB1",115200)

##aline =  ""
##while True:
##    achar = serua.read()
##    if achar == chr(13):
##        print (aline)
##        serxbee.write(aline+"\n")
##        aline = ""
##    else:
##        aline = aline + achar
##    
lineua = ""
linews = ""

while True:
    if serua.inWaiting():#equivalent to if serial data is available
        charua = serua.read()
        if charua in "\n"+ chr(13):
            print(lineua)
            lineua =""
        else:
            lineua = lineua + charua
            
    if serws.inWaiting():
        charws = serws.read()
        if charws in "\n"+ chr(13):
            print(linews)
            linews =""
        else:
            linews = linews + charws

    
