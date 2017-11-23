#
# example of loops
#

def main():
    x = 0
    while(x < 5):
        print x
        x = x + 1

    for x in range(5,10):
        print x

    days = ["Mon", "Tues", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for d in days:
        print d

    #break and continue
    for x in range(5,10):
        if(x == 7): break
        print x

    for x in range(5,10):
        if(x % 2 == 0): continue
        print x

    days = ["Mon", "Tues", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for i, d in enumerate(days):
        print i, d
    
if __name__ == "__main__":
    main()
