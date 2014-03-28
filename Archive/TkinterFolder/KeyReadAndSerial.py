from Tkinter import *
import serial
from datetime import datetime, date, time, timedelta

root = Tk()

def key(event):
    print "pressed",repr(event.char)

def callback(event):
    frame.focus_set()
    print "clicked at", event.x, event.y

frame = Frame(root, width =100, height = 100)
frame.bind("<Key>",key)
frame.bind("<Button-1>",callback)
frame.pack()

root.mainloop()


#declaring global variables
ser = serial.Serial("/dev/ttyAMA0",115200)

foldername = "/home/pi/FYP_PythonCode/Repo1UART/OutputData/"
filestub = "Data"
fileext = ".txt"
filename = filestub + datetime.now().strftime("%Y_%m_%d_%H_%M") + fileext

#time save incrementer. #assume new file name is just the date and time
#that means it will always be unique. ensure that t
minstoincrement = 2
nextinctime = datetime.now() + timedelta(minutes=minstoincrement)


#this section reads the Serial Data from the UART pins, displays it and saves it
line = ""

#I believe that this needs to be looped in root.
while True:    
    data = ser.read()
    if (data=="\n"): #any write command
        #if current time is greater than nextinctime ->
        #1. change file name
        #2. and reset inc time.
        if (datetime.now() > nextinctime):
            filename = filestub + datetime.now().strftime("%Y_%m_%d_%H_%M") + fileext
            nextinctime = datetime.now() + timedelta(minutes=minstoincrement)
            print("File name changed to: " +filename)
        #print to screen
        print(line)
        #create the datetimestrings.
        nowdate = str(datetime.now().date())
        nowtime = datetime.now().strftime("%H:%M")
        #concats filenames
        filepath = foldername + filename
        #writes to file
        f=open(filepath,'a')
        f.write(nowdate+"," + nowtime+","+line+"\n")
        f.close()
        
        line = ""
    else:
        line = line + data
