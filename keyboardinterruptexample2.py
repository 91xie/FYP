#Super important as this allows one to interface with the program.
import time

while True:
    try:
        print "hello"
        time.sleep(1)        
    except KeyboardInterrupt:
        sometext = raw_input ("what do key do you want to press?")
        print (sometext)

        if sometext in "qQ":
            break
        pass
