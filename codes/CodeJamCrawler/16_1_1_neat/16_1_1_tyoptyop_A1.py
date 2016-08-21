#!/usr/bin/env python
#
# >

import sys

    
h = file(sys.argv[1], "r")
flag = True
results = []
for line in h.readlines():
    if flag == True:
        flag = False
        continue ;
    line = line[:-1]
    result = ""
    for char in line:
        if len(result) == 0:
            result = char
            continue ;
        if char >= result[0]:
            result = char + result
        elif char < result[0]:
            result += char
    results.append(result)
    

for i in range(0,len(results)):
    print "Case #%d: %s" % (i+1, results[i])
    

