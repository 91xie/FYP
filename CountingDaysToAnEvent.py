import time
from datetime import date
today = date.today()
print(today)

    #you could see here the boolean operators
aboolean = today == date.fromtimestamp(time.time())
print('today is', str(date.fromtimestamp(time.time())))
print(aboolean)


birthdaymonth = input('what number month is your birthday?')
birthdayday = input('what number date is your birthday?')


my_birthday = date(today.year, birthdaymonth,birthdayday)
print('your birthday is ...' , str(my_birthday))
if my_birthday < today:
        #this is how you set reset the year and days of a date object
        #hopefully this would work with time too!
    my_birthday = my_birthday.replace(year=today.year + 1)

time_to_birthday = abs(my_birthday - today)



if my_birthday == today:
    print("Congradulations! Today is your birthday! :D")
else:
    print "sorry, today is not your birthday :("
    print "time to your birthday is ", time_to_birthday
