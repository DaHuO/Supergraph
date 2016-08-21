#!/usr/bin/env python
#
# >

import sys

    
h = file(sys.argv[1], "r")
flag = True
results = []
lines = []
for line in h.readlines():
    if flag == True:
        flag = False
        continue ;
    line = line[:-1]
    sorted_line = sorted(list(line))
    num = []
    old = -1
    while len(num) > old:
        old = len(num)
        if 'W' in sorted_line:
            sorted_line.remove('T')
            sorted_line.remove('W')
            sorted_line.remove('O')
            num.append("2")
        if 'Z' in sorted_line:
            sorted_line.remove('Z')
            sorted_line.remove('E')
            sorted_line.remove('R')
            sorted_line.remove('O')
            num.append("0")
        if 'X' in sorted_line:
            sorted_line.remove('S')
            sorted_line.remove('I')
            sorted_line.remove('X')
            num.append("6")
        if 'G' in sorted_line:
            sorted_line.remove('E')
            sorted_line.remove('I')
            sorted_line.remove('G')
            sorted_line.remove('H')
            sorted_line.remove('T')
            num.append("8")
        if 'U' in sorted_line:
            sorted_line.remove('F')
            sorted_line.remove('O')
            sorted_line.remove('U')
            sorted_line.remove('R')
            num.append("4")
    old = -1
    while len(num) > old:
        old = len(num)
        if 'H' in sorted_line:
            sorted_line.remove('T')
            sorted_line.remove('H')
            sorted_line.remove('R')
            sorted_line.remove('E')
            sorted_line.remove('E')
            num.append("3")
        if 'F' in sorted_line:
            sorted_line.remove('F')
            sorted_line.remove('I')
            sorted_line.remove('V')
            sorted_line.remove('E')
            num.append("5")
    old = -1
    while len(num) > old:
        old = len(num)
        if 'V' in sorted_line:
            sorted_line.remove('S')
            sorted_line.remove('E')
            sorted_line.remove('V')
            sorted_line.remove('E')
            sorted_line.remove('N')
            num.append("7")
        if 'I' in sorted_line:
            sorted_line.remove('N')
            sorted_line.remove('I')
            sorted_line.remove('N')
            sorted_line.remove('E')
            num.append("9")
        if 'O' in sorted_line:
            sorted_line.remove('O')
            sorted_line.remove('N')
            sorted_line.remove('E')
            num.append("1")
        if len(sorted_line) == 0:
            break
    results.append("".join(sorted(num)))
for i in range(0,len(results)):
    print "Case #%d: %s" % (i+1, results[i])
    

