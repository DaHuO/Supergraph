#!/usr/bin/env python
#
# URL: 
#

import math
import sys
import logging
import re
from collections import defaultdict
import tempfile

testdata = '''22
1 1 1 10
1 2 3 2
1 1 3 2
1 2 3 1
2 2 2 1
2 2 2 2
2 2 2 3
2 3 4 7
2 3 4 1
2 3 6 2
2 3 6 12
3 4 8 1
3 4 8 2
3 4 8 3
3 4 8 4
3 4 8 5
3 4 8 6
3 4 8 7
3 4 8 8
3 4 8 9
3 4 8 10
3 4 8 11
3 4 8 12
3 5 6 12
2 3 3 1
2 3 3 5
'''

def gcd(x,y):
    while x > 0 and y > 0:
        x,y = y,(x%y)
    if x == 0:
        return y
    return x

def readstr(fhandle):
    return fhandle.readline().strip()

def readone(fhandle):
    return int(fhandle.readline().strip())

def readint(fhandle):
    return readone(fhandle)

def readmult(fhandle):
    return tuple(fhandle.readline().strip().split())

def readmultint(fhandle):
    return tuple(int(x) for x in readmult(fhandle))

def readfirst(fhandle):
    ncases = readone(fhandle)
    return ncases

def nextcase(fhandle,params=None):
    x,y,z,N = readmultint(fhandle)
    logging.info('Test: %d %d %d %d', x, y, z, N)
    return solve(x,y,z,N)

def solve(x,y,z,N):
    retlist = []
    # bound by second largest value y ...
    if z == 1:
        return [(1,1,1)]
    M = N * x * y
    M = min(M,x*y*z)

    '''
    for _z in range(z,y+1,-1):
        if gcd(x,_z) == 1 and gcd(y,_z) == 1:
            logging.debug('switching z %s', _z)
            z = _z
            break
    '''

    g1 = gcd(x,z)
    g2 = gcd(y,z)
    g3 = gcd(g1,g2)
    logging.debug('gcd %d, %d', g1, g2)

    for i in range(M):
        a = (i/y) % x
        b = (i) % y
        if g1 == 1 and g2 == 1:
            c = (i) % z
        elif g1 == 1:
            c = (i+(i/(x*z))) % z
            #c = (i+(i/z)+(i/(x*z))) % z
            c = (i+(i/y)) % z
            #c = (i+(i/z)+(i/(x*z))+(i/(x*y*g2))) % z
            #c = (i+(i/z)+(i/(x*y))) % z
        elif g2 == 1:
            c = (i+(i/(y*z))) % z
            #c = (i+(i/z)+(i/(x*y))) % z
        elif g3 == 1:
            c = (i+(i/z)+(i/(x*y))+(i/(y*z))) % z
        else:
            c = (i+(i/z)+(i/(x*y))) % z
            #c = (i+(i/z)+(i/(x*y))+(i/(x*y*z))) % z
        retlist.append((a+1,b+1,c+1))

    # validate
    logging.debug('returning: %d', len(retlist))
    counts = defaultdict(lambda:0)
    for i,(a,b,c) in enumerate(retlist):
        logging.debug('%d %d %d', a, b, c)
        if (a,b,c) in counts:
            raise Exception("%d: %d %d %d found twice" % (i,a,b,c))
        counts[a,b,c] = 1
        counts[a,b,0] += 1
        counts[a,0,c] += 1
        counts[0,b,c] += 1
        if counts[a,b,0] > N or counts[a,0,c] > N or counts[0,b,c] > N:
            raise Exception("%d: %d %d %d over" % (i,a,b,c))
    logging.debug('validate: %s', counts.values())
    logging.debug('validate: %d %d', max(counts.values()), N)
    assert max(counts.values()) <= N
    return retlist

if __name__ == '__main__':
    
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--test',help='test cases',action='store_true',default=False)
    parser.add_argument('-d','--debug',action='count',default=0)
    parser.add_argument('inputfile',nargs='?')
    args = parser.parse_args()

    if args.debug >= 1:
        logging.basicConfig(level=logging.DEBUG,stream=sys.stdout)
    else:
        logging.basicConfig(level=logging.CRITICAL,stream=sys.stderr)

    ifhandle = sys.stdin
    if args.inputfile:
        ifhandle = open(args.inputfile)
    if args.test:
        ifhandle = tempfile.TemporaryFile()
        ifhandle.write(testdata)
        ifhandle.seek(0)
    ofhandle = sys.stdout

    nparams, ncases = 0, readfirst(ifhandle)

    # parameter reading
    logging.debug('%d parameters', nparams)
    for i in range(nparams):
        pass

    # test case reading
    logging.debug('%d cases', ncases)
    for i in range(ncases):
        ans = nextcase(ifhandle)
        outstr = 'Case #%d: %d' % (i+1, len(ans))
        for x in ans:
            outstr = outstr + '\n%d %d %d' % x
        #logging.info(outstr)
        print >>ofhandle, outstr

    logging.info('Complete')
