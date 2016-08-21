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
    input_line = int(line)
    if input_line == 0:
        results.append("INSOMNIA")
        continue ;
    numbers = []
    for i in range(1,65536):
        tmp = input_line * i
        for char in str(tmp):
            char_int = int(char)
            if char_int not in numbers:
                numbers.append(char_int)
                if len(numbers) == 10:
                    results.append(str(tmp))
                    break ;
        if len(numbers) == 10:
            break ;
for i in range(0,len(results)):
    print "Case #%d: %s" % (i+1, results[i])
    

