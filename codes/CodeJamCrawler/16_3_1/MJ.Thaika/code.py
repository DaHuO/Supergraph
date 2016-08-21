#!python
import sys
from optparse import OptionParser
from collections import deque
import math
import operator
import itertools
import string
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

T = int(f.readline())
for j in range(1,T+1):
    N = int(f.readline())

    arr = f.readline().split()

    for i in range(N):
        arr[i] = (int(arr[i]),string.ascii_uppercase[i])
    arr.sort(reverse=True)

    print 'Case #%d:' % (j),

    while (arr[0][0]>0):
        if (arr[0][0]>arr[1][0]):
            print arr[0][1],
            arr[0] = (arr[0][0]-1,arr[0][1])
        else:
            if len(arr)>2:
                if (arr[2][0]==arr[1][0]):
                    print arr[0][1],
                    arr[0] = (arr[0][0]-1,arr[0][1])
                else:
                    print arr[0][1]+arr[1][1],
                    arr[0] = (arr[0][0]-1,arr[0][1])
                    arr[1] = (arr[1][0]-1,arr[1][1])
            else:
                print arr[0][1]+arr[1][1],
                arr[0] = (arr[0][0]-1,arr[0][1])
                arr[1] = (arr[1][0]-1,arr[1][1])
        arr.sort(reverse=True)
    print ""