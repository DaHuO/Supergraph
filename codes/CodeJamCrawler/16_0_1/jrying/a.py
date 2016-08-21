import sys
import fileinput
import re

#fileio
fileName = 'A-large'
# fileName = 'A-small-attempt0'
# fileName = 'A-test'
input = fileName + ".in"
output = fileName + ".out"

###
with open(input) as fi, open(output, "w") as fo:
    count = 0
    for line in fi.readlines()[1:]:
        print line
        arr = [False] * 10;
        n = int(line)
        result = 0
        ###
        if n != 0:
            for i in xrange(1, 10**9):
                for c in set(list(str(n*i))):
                    arr[int(c)] = True
                if all(arr):
                    result = n*i
                    break
        result = result if result else "INSOMNIA"
        ###
        #normal
        count += 1
        resultStr = "Case #"+str(count)+": "+str(result)
        print resultStr
        fo.write(resultStr+'\n')
