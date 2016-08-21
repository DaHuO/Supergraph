#!/usr/bin/env python
#
# >

import sys

    
h = file(sys.argv[1], "r")
flag = True
flag2 = True
nb_lines = 0
results = []
lines = []
for line in h.readlines():
    if flag == True:
        flag = False
        continue ;
    line = line[:-1]
    if flag2 == True:
        nb_lines = int(line) * 2 - 1
        flag2 = False
        continue ;
    if nb_lines > 0:
        nb_lines -= 1
        lines.append(line.split(" "))
    if nb_lines == 0:
        # print lines
        nums = []
        for i in lines:
            for j in i:
                j = int(j)
                if j in nums:
                    nums.remove(int(j))
                else:
                    nums.append(int(j))
        nums.sort()
        tmp = []
        for i in nums:
            tmp.append(str(i))
        results.append(" ".join(tmp))
        flag2 = True
        lines = []
    

for i in range(0,len(results)):
    print "Case #%d: %s" % (i+1, results[i])
    

