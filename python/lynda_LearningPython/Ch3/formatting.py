#
# Now let's look at example of string formtting
#

from datetime import datetime

def main():
    now = datetime.now()

    #Date formatting
    print now.strftime("%Y") #full year with century
    print now.strftime("%y") #year without century
    #more complicated example
    print now.strftime("%a, %d, %B, %y") #abrv. day, day of month, full month, abrv. year
    #localised versions
    print now.strftime("%c")
    print now.strftime("%x")
    print now.strftime("%X")

    #Moving on to time info, not just date info
    print now.strftime("%I:%M:%S %p")
    print now.strftime("%H:%M")
    
if __name__ == "__main__":
    main();
