print "start"
aline = ""

while True:
    aread = raw_input("Write here:")
    for achar in aread:
        aline = aline + str(ord(achar))+","
    print aline
    aline = ""
