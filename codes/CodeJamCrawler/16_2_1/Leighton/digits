#!/usr/bin/env python

import sys
if len(sys.argv) == 2:
    file = open(sys.argv[-1])
else:
    print "Usage: digits filename.in"
    sys.exit(0)

lines = [line.strip() for line in file]
file.close()
s = int(lines.pop(0))

def find(anagram):
    t = sorted(anagram)
    found = []
    while "Z" in t:
        found.append(0)
        t.remove('Z')
        t.remove('E')
        t.remove('R')
        t.remove('O')
    while "G" in t:
        found.append(8)
        t.remove('E')
        t.remove('I')
        t.remove('G')
        t.remove('H')
        t.remove('T')
    while "H" in t:
        found.append(3)
        t.remove('T')
        t.remove('H')
        t.remove('R')
        t.remove('E')
        t.remove('E')
    while "W" in t:
        found.append(2)
        t.remove('T')
        t.remove('W')
        t.remove('O')
    while "X" in t:
        found.append(6)
        t.remove('S')
        t.remove('I')
        t.remove('X')
    while "R" in t:
        found.append(4)
        t.remove('F')
        t.remove('O')
        t.remove('U')
        t.remove('R')
    while "F" in t:
        found.append(5)
        t.remove('F')
        t.remove('I')
        t.remove('V')
        t.remove('E')
    while "V" in t:
        found.append(7)
        t.remove('S')
        t.remove('E')
        t.remove('V')
        t.remove('E')
        t.remove('N')
    while "I" in t:
        found.append(9)
        t.remove('N')
        t.remove('I')
        t.remove('N')
        t.remove('E')
    while "O" in t:
        found.append(1)
        t.remove('O')
        t.remove('N')
        t.remove('E')
    if len(t) != 0:
        print "NON-ZERO!!!!!!: %d" % (len(t))
    found.sort()
    found = [str(i) for i in found]
    return ''.join(found)

output = []
for i in xrange(s):
    print "Case #%d: %s" % (i + 1, find(lines[i]))
