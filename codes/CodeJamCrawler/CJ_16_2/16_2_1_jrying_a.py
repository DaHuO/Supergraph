import sys
import fileinput
import re

#fileio
fileName = 'A-large'
# fileName = 'A-small-attempt0'
# fileName = 'A-test'
input = fileName + ".in"
output = fileName + ".out"

def format(s):
    return map(lambda i: s.count(chr(ord('A')+i)), range(26));

digits = map(format, ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"])

def substract(a, r, i, n):
    while (a[i]):
        a = map(lambda i: a[i]-digits[n][i], range(26))
        r.append(str(n))
    return a, r

def foo(a):
    r = []
    #Z
    a, r = substract(a, r, 25, 0)
    #X
    a, r = substract(a, r, 23, 6)
    #W
    a, r = substract(a, r, 22, 2)
    #U
    a, r = substract(a, r, 20, 4)
    #R
    a, r = substract(a, r, 17, 3)
    #T
    a, r = substract(a, r, 19, 8)
    #S
    a, r = substract(a, r, 18, 7)
    #O
    a, r = substract(a, r, 14, 1)
    #F
    a, r = substract(a, r, 5, 5)
    #I
    a, r = substract(a, r, 8, 9)
    return r


###
with open(input) as fi, open(output, "w") as fo:
    count = 0
    for line in fi.readlines()[1:]:
        print line
        arr = [False] * 10;
        result = 0
        ###
        print format(line)
        result = "".join(sorted(foo(format(line))))

        ###
        #normal
        count += 1
        resultStr = "Case #"+str(count)+": "+str(result)
        print resultStr
        fo.write(resultStr+'\n')
