#!/usr/bin/python

import sys

def f(n):
    if n == 0:
        return 'INSOMNIA'
    d = {0 : False, 1 : False, 2 : False, 3 : False, 4 : False, 5 : False, 6: False, 7 : False, 8 : False, 9 : False}
    j = 0
    cnt = 0
    while cnt < 10:
        j += 1
        s = str(n*j)
        for i in range(len(s)):
            if d[int(s[i])] == False:
                cnt += 1
                d[int(s[i])] = True
    return n*j
   
 
file_name =  sys.argv[1]
with open(file_name, 'r') as fl:
    fl.readline()
    for i, line in enumerate(fl):
        output = "Case #%d: "%(i+1)
        n = int(line)
        output += "%s"%f(n)
        print output