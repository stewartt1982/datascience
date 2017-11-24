#
# Example of working with filesystem shell methods
#

import os
import shutil
from os import path
from shutil import make_archive
from zipfile import ZipFile

def main():
    if path.exists("newfile.txt"):
        src = path.realpath("newfile.txt")

        # #break path into directory path and filename
        # head, tail = path.split(src)
        # print "path: " + head
        # print "file: " + tail

        # #make a copy, duplicate
        # dst = src + ".bak"
        # shutil.copystat(src,dst)

        # #rename
        # os.rename("textfile.txt","newfile.txt")

        #zip archive
        #root_dir, tail = path.split(src)
        #shutil.make_archive("archive","tar",root_dir)

        with ZipFile("testzip.zip","w") as newzip:
            newzip.write("newfile.txt")
            newzip.write("textfile.txt.bak")
            
if __name__ == "__main__":
    main()
