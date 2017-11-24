#
# example using os module, paths
#

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
    print os.name;

    #path module
    print "Item exists: " + str(path.exists("textfile.txt"))
    print "Item is a file: " + str(path.isfile("textfile.txt"))
    print "Item a directoryt: " + str(path.isdir("textfile.txt"))

    #work with directories
    print "Item's path: " + str(path.realpath("textfile.txt"))
    print "Item's path and name: " + str(path.split(path.realpath("textfile.txt")))

    #last modification time
    t = time.ctime(path.getmtime("textfile.txt"))
    print t
    print datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    #calc how long abou this was
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print "It has been "+ str(td) + " since this file was updated"
    print "Or to put it another way " + str(td.total_seconds()) + " seconds"
    
if __name__ == "__main__":
    main()
    

