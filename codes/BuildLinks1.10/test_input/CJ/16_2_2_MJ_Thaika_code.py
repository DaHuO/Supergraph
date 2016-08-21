#!python
import sys
from optparse import OptionParser
from collections import deque
import math
import operator
import itertools
import re
usage = 'usage: %prog input'
parser = OptionParser(usage=usage)
(options, args) = parser.parse_args()
if args:
    if args[0] == '-':
        f = sys.stdin
    else:
        f = open(args[0])
elif not sys.stdin.isatty():
    f = sys.stdin
else:
    parser.error('Need input from file or stdin')

currans = sys.maxint
ca = ''
ja = ''

def minnum(c,j):
    done = 0
    for i in range(len(c)):
        if c[i]=='?':
            if j[i]=='?':
                tmp = list(c)
                tmp[i] = '0'
                c = ''.join(tmp)

                tmp = list(j)
                tmp[i] = '0'
                j = ''.join(tmp)
                minnum(c,j)

                tmp = list(c)
                tmp[i] = '1'
                c = ''.join(tmp)
                
                tmp = list(j)
                tmp[i] = '0'
                j = ''.join(tmp)
                minnum(c,j)

                tmp = list(c)
                tmp[i] = '0'
                c = ''.join(tmp)
                
                tmp = list(j)
                tmp[i] = '1'
                j = ''.join(tmp)
                minnum(c,j)

                tmp = list(c)
                tmp[i] = '9'
                c = ''.join(tmp)
                
                tmp = list(j)
                tmp[i] = '0'
                j = ''.join(tmp)
                minnum(c,j)

                tmp = list(c)
                tmp[i] = '0'
                c = ''.join(tmp)
                
                tmp = list(j)
                tmp[i] = '9'
                j = ''.join(tmp)
                minnum(c,j)
            else:
                if j[i]=='0':
                    tmp = list(c)
                    tmp[i] = '0'
                    c = ''.join(tmp)
                    minnum(c,j)

                    tmp = list(c)
                    tmp[i] = '1'
                    c = ''.join(tmp)
                    minnum(c,j)

                    tmp = list(c)
                    tmp[i] = '1'
                    c = ''.join(tmp)
                    minnum(c,j)
                elif j[i]=='9':
                    tmp = list(c)
                    tmp[i] = '8'
                    c = ''.join(tmp)
                    minnum(c,j)

                    tmp = list(c)
                    tmp[i] = '9'
                    c = ''.join(tmp)
                    minnum(c,j)
                else:
                    tmp = list(c)
                    tmp[i] = str(int(j[i])-1)
                    c = ''.join(tmp)
                    minnum(c,j)

                    tmp = list(c)
                    tmp[i] = j[i]
                    c = ''.join(tmp)
                    minnum(c,j)

                    tmp = list(c)
                    tmp[i] = str(int(j[i])+1)
                    c = ''.join(tmp)
                    minnum(c,j)

                tmp = list(c)
                tmp[i] = '0'
                c = ''.join(tmp)
                minnum(c,j)

                tmp = list(c)
                tmp[i] = '9'
                c = ''.join(tmp)
                minnum(c,j)
        else:
            if j[i]=='?':
                if c[i]=='0':
                    tmp = list(j)
                    tmp[i] = '0'
                    j = ''.join(tmp)
                    minnum(c,j)

                    tmp = list(j)
                    tmp[i] = '1'
                    j = ''.join(tmp)
                    minnum(c,j)
                elif c[i]=='9':
                    tmp = list(j)
                    tmp[i] = '8'
                    j = ''.join(tmp)
                    minnum(c,j)

                    tmp = list(j)
                    tmp[i] = '9'
                    j = ''.join(tmp)
                    minnum(c,j)
                else:
                    tmp = list(j)
                    tmp[i] = str(int(c[i])-1)
                    j = ''.join(tmp)
                    minnum(c,j)

                    tmp = list(j)
                    tmp[i] = c[i]
                    j = ''.join(tmp)
                    minnum(c,j)

                    tmp = list(j)
                    tmp[i] = str(int(c[i])+1)
                    j = ''.join(tmp)
                    minnum(c,j)

                tmp = list(j)
                tmp[i] = '0'
                j = ''.join(tmp)
                minnum(c,j)

                tmp = list(j)
                tmp[i] = '9'
                j = ''.join(tmp)
                minnum(c,j)
            else:
                done = 1
    if done==0:
        return
    global currans
    global ca
    global ja
    # print c,j
    if (abs(int(c)-int(j))<currans):
        ca = c
        ja = j
        currans = abs(int(c)-int(j))
    elif (abs(int(c)-int(j))==currans):
        if (int(c)<int(ca)):
            ca = c
            ja = j
            currans = abs(int(c)-int(j))


T = int(f.readline())
for i in range(1,T+1):
    line = f.readline()
    c,j = line.split()
    # print c,j

    currans = sys.maxint
    ca = ''
    ja = ''

    minnum(c,j)
    print 'Case #%d: %s %s' % (i,ca,ja)