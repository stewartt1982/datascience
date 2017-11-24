#
# Example of paring and processing html
#

from HTMLParser import HTMLParser

metacount = 0

#define out MyParser Class
class MyHTMLParser(HTMLParser): # inherits from HTMLParser
    def handle_comment(self, data):
        print "Encountered comment: ", data
        pos = self.getpos()
        print "At line: ",pos[0], " position ",pos[1]

    def handle_data(self,data):
        print "Encountered some data:",data
        pos = self.getpos()
        print "At line: ",pos[0]," position ",pos[1]

    def handle_endtag(self,tag):
        print "Encountered an endtag:",tag
        pos = self.getpos()
        print "At line: ",pos[0]," position ",pos[1]

    def handle_starttag(self,tag,attrs):
        global metacount
        print "Encountered a starttag:",tag
        if tag == "meta":
            metacount +=1
            
        pos = self.getpos()
        print "At line: ",pos[0]," position ",pos[1]
        if attrs.__len__ > 0:
            print "\tAttributes:"
            for a in attrs:
                print "\t", a[0],"=",a[1]
        
def main():
    #start HTML parser
    parser = MyHTMLParser()
    #open html file
    f = open("samplehtml.html")
    if f.mode == "r":
        #file is opened for reading
        contents = f.read()
        parser.feed(contents)

    #print out number of metatags encountered
    print "%d meta tags encountered" % metacount
        
if __name__ == "__main__":
    main();
