#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

def main():
    print timedelta(days=365, hours=5, minutes=1)
    print "today's date is "+ str(datetime.now())
    #example using timedelta.  What will be today's date one year from now
    print "one year from now it will be: " + str(datetime.now() + timedelta(days=365))
    print "in two weeks and 3 days it will be: " + str(datetime.now() + timedelta(weeks = 2, days=2))
    t = datetime.now() - timedelta(weeks = 1)
    s = t.strftime("%A %B %d %Y")
    print "one week ago was " + s

    #how many days until the next april fools day
    today = date.today()
    afd = date(today.year,4,1) #April fools days this year
    #check if April fools day has already past, if so we want to get the date of the next years
    #April fool days
    if afd < today:
        print "April fools day has already went by %d days ago" % ((today - afd).days)
        afd = afd.replace(year=today.year + 1)

    #now we have the next April fools days
    ttoafd = abs(afd - today)
    print ttoafd.days, "days until the next april fools day"
    
    
if __name__ == "__main__":
    main();
