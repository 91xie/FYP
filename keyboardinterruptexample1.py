import time

try:
    while True:
        print "hello"
        time.sleep(1)        
except KeyboardInterrupt:
    sometext = input ("what do key do you want to press?")
    print (sometext)
    pass
