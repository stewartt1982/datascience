#
# Example of parsing and processing JSON
#

import urllib2
import json

def printResults(data):
    #use the jason module to load the string data into a dictionary
    theJSON= json.loads(data)

    #now we have a python object
    if "title" in theJSON["metadata"]:
        print theJSON["metadata"]["title"]
    #Numer of events and the magnitude of each event name
    count = theJSON["metadata"]["count"]
    print str(count) + " events recorded"
    #print where it occurred
    for i in theJSON["features"]:
        print i["properties"]["place"]
    #only > 4
    for i in theJSON["features"]:
        if i["properties"]["mag"] >= 4.0:
            print "%2.1f" % i["properties"]["mag"], i["properties"]["place"]

    #only events where it was felt by someone
    print "Events that were felt:"
    for i in theJSON["features"]:
        feltReports = i["properties"]["felt"]
        if(feltReports != None) & (feltReports > 0):
            print "%2.1f" % i["properties"]["mag"], i["properties"]["place"], " reported "  + str(feltReports) + " times" 

def main():
    urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    #
    webUrl = urllib2.urlopen(urlData)
    print webUrl.getcode()
    if(webUrl.getcode()==200):
        data = webUrl.read()
        printResults(data)
    else:
        print "Recieved an error from the server, cannot retrieve results "+str(webUrl.getcode())
    
if __name__ == "__main__":
    main();
