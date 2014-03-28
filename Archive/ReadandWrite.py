import calendar
import datetime
import time

f = open('/home/pi/Desktop/details.txt','r')
print(f)
print(f.read()) #this is how to read

#you could also print out line by line
for line in f:
    print(line)

f.close();

#'r' is for read only, 'w' for writing/overwrite 'a' appends 'r+' read and write
#
f = open('/home/pi/Desktop/data.txt','a')
f.write('This is a test input');
f.close();


#print local current time as a struct.
#will get you the following output ('Local current time: ', time.struct_time(tm_year=2013, tm_mon=6, tm_mday=19, tm_hour=19, tm_min=33, tm_sec=16, tm_wday=2, tm_yday=170, tm_isdst=0))
print('-----------------')

localtime = time.localtime(time.time())
print("Local current time: ", localtime)

    #here I am going to print out formatted.

print("the hour is as follows", localtime.tm_hour)

    #now I'm going to add an hour

#localtime.tm_hour = localtime.tm_hour + 1
#print("after I have added an hour to localtime.tm_hour", localtime.tm_hour)
    #can't do this as it is a readonly attribute.


#print a calendar
print('-----------------')
print(calendar.month(2008,1))


# you could try convert the thing into seconds first?
