#examples for working wtih datetime objects
from datetime import datetime, date, time, timedelta
#using datetime.combine()
d = date( 2005, 7, 14)
t = time(12,30)

adatetime = datetime.combine(d,t)
print ('adatetime           ',adatetime)
print ('str(adatetime)      ',str(adatetime))
#using datetime.now() or datetime.utcnow()
print ('datetime.now()      ',datetime.now())
print ('datetime.utcnow()   ',datetime.utcnow())

#using datetime. strptime()
dt = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
print ('datetime.strptime   ', dt)

#using datetime.timeuple() to get all attributes
tt = dt.timetuple()
for it in tt:
    print it

#date in iso formate
ic = dt.isocalendar()

for it in ic:
    print it

#you could save the information as a text file, you can have an option
    #of including the date and time with each reading.
    #you also need to have the same checks to ensure that the date is being added
    #at the right time

#######################from the standard example.

print ('-----------------------')

##how tot get hour and min in string format
print datetime.now()
nowhour = str(datetime.now().hour)
nowmin = str(datetime.now().minute)

print nowhour + ":" + nowmin

#string formatting made easy
#google "python strftime"
print datetime.now().strftime("%Y_%m_%d_%H_%M")


##incrementing a date time add minute
now = datetime.now()
now_plus_10 = datetime.now() + timedelta(hours = 10)
print (now)
print (now_plus_10)

