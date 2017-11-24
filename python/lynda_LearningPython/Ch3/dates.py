#
# example of using included python classes (dates and times)
#

from datetime import date
from datetime import time
from datetime import datetime

def main():
    #date objects.  Get todays date
    today = date.today()
    print "Today's date is ",today

    #get date by indiv. comp.
    print "Date Components ",today.day, today.month, today.year

    #other bits
    print "Today's Weekday number: ",today.weekday()

    #Now we can play with datetime class
    today = datetime.now()
    print "The current date and time is ", today
    t = datetime.time(datetime.now())
    print "the current time is ",t

    #weekday returns 0 - 6, ie. mon to sun
    wd = date.weekday(today)
    days = ["Mon","Tue","Wed", "Thu","Fri","Sat","Sun"]
    print "Today is day number %d" % wd, "which is a " + days[wd]
    
if __name__ == "__main__":
    main()
