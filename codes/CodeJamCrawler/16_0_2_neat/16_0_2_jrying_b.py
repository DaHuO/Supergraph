import sys
import fileinput
import re

#fileio
fileName = 'B-large'
# fileName = 'B-small-attempt0'
# fileName = 'B-test'
input = fileName + ".in"
output = fileName + ".out"

###
with open(input) as fi, open(output, "w") as fo:
    count = 0
    for line in fi.readlines()[1:]:
        print line
        result = 0
        line = line.strip()
        ###
        last = "."
        for c in line:
            if c != last:
                result += 1
            last = c
        if line[-1] == "+":
            result -= 1
        ###
        #normal
        count += 1
        resultStr = "Case #"+str(count)+": "+str(result)
        print resultStr
        fo.write(resultStr+'\n')
