#!/bin/env python2
'''
Simplistic replace of all font colours with black in the stylesheet.
'''
import os
import sys
import shutil
import tempfile
from zipfile import ZipFile, is_zipfile


def to_black(infile):
    zf = ZipFile(infile, mode='r')
    zf.extractall("tmp/")
    zf.close()
    ssfile = open("tmp/stylesheet.css",'r')
    data = ssfile.readlines()
    for idx, item in enumerate(data):
        if 'color:' in item:
            item = "    color: black;\n"
            data[idx] = item
        #if 'font-family:'  in enumerate(data):
        #    data[idx] = ''
        #print item,
    ssfile.close()
    ssfile = open("tmp/stylesheet.css",'w')
    ssfile.writelines(data)
    ssfile.close()
    zf = ZipFile(infile, mode='w')
    for path, subdirs, files in os.walk('tmp/'):
        for filename in files:
            print os.path.join(path, filename)
            zf.write(os.path.join(path, filename),filename)
    zf.close()
    #shutil.rmtree('tmp')
    print "Done!  Now test it."



    return

if __name__ == '__main__':
    print to_black(sys.argv[1])
