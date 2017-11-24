#
# Example file for retrieving data from the internet
#

import urllib2

def main():
    #open a connection to URL
    webUrl = urllib2.urlopen("http://joemarini.com")
    #get the result code and print it if 200 it is ok
    print "result code: "+ str(webUrl.getcode())
    #read data from url
    data = webUrl.read()
    print data
    
if __name__ == "__main__":
    main()
