#untitled4

def isdigitval(aval):
    aval = aval.replace("-","")
    aval = aval.replace(".","")
    aval = aval.replace(" ","")
    if aval.isdigit():
        print "isdigit"
    else:
        print "notdigit"

astr = "-"
isdigitval(astr)
