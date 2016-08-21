import sys
import os
from os import listdir
from os.path import isfile, join


def linecount(folder):
    target_files = [folder + '/' + f for f in listdir(folder) if isfile(join(folder, f))]
    if '.DS_Store' in target_files:
        target_files.remove('.DS_Store')
    count = 0
    for f in target_files:
        fin = open(f, 'r')
        for line in fin:
            count += 1
        fin.close()
    print 'total lines of codes:'
    print count

if __name__ == '__main__':
    #    folder = 'sort_codes'
    folder = 'CodeJam/2A/python'
    linecount(folder)
