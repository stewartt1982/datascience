#
# example of opening, reading, writing to files
#

def main():
    #open file for writing, create if it does not exist
    f = open("textifle.txt","w+")
    #write
    for i in range(10):
        f.write("This is a line %d\n" % (i+1))
    f.close();

    #open for append

    f = open("textfile.txt","a+")
    for i in range(10):
        f.write("This is a line %d\n" % (i+1))
    f.close();

    #read a file
    f = open("textfile.txt","r")
    print "By contents, read all file in\n"
    if f.mode == 'r': #check if file is opened for read
        contents = f.read()
        print contents

    f.close()

    #by line
    f = open("textfile.txt","r")
    print "print file by each line\n"
    lines = f.readlines()
    for line in lines:
        print line
    
if __name__ == "__main__":
    main();
