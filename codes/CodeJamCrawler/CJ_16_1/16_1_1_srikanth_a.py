#!/usr/bin/python
import sys

ipfile = sys.stdin
opfile = sys.stdout

T = int(ipfile.readline().strip())

for t in xrange(1,T+1):
    ipstr = ipfile.readline().strip()
    opstr = ""
    for c in ipstr:
        if opstr == "":
            opstr += c
            continue
        if opstr[0]<=c:
            opstr = c + opstr
        else:
            opstr = opstr + c
    
    opfile.write('Case #%d: %s\n' % (t,opstr))

                




