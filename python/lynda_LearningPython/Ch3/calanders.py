#
# Example working with calendars
#

import calendar

#create a calendar, plain text
c = calendar.TextCalendar(calendar.SUNDAY)
str = c.formatmonth(2013,1,0,0)
print str

#HTML calendar
hc = calendar.HTMLCalendar(calendar.SUNDAY)
str = hc.formatmonth(2013,1)
print str

#loop over days of the month
for i in c.itermonthdays(2013, 8):
    #week starts on a sunday, as defined above.  Gives leading 0s
    print i

for name in calendar.month_name:
    print name

for day in calendar.day_name:
    print day


#a more realistic example of calander manipulation: A team meets on the
#first friday of every month.  We will figure out what days that would be for each month
for m in range(1,13): #ie. 1 inclusive to 13 exclusive
    #returns an array of weeks for each month m
    cal = calendar.monthcalendar(2013, m)
    #first Friday has to be in the first two weeks
    weekone = cal[0]
    weektwo = cal[1]

    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]

    print "%10s %2d" % (calendar.month_name[m], meetday)
