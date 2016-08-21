# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 00:34:46 2016

@author: jiang
"""

# raw_input() reads a string with a line of input, 
#stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
#t = int(raw_input())  # read a line with a single integer
#for i in xrange(1, t + 1):
#  n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
#  
#  print "Case #{}: {} {}".format(i, n + m, n * m)
  # check out .format's specification for more formatting options
  
import fileinput
def testNum(n,dic):
    s = str(n)
    for c in s:
        if c in dic:
            pass
        else:
            dic.append(c)
    return len(dic)
if __name__ == "__main__" :
    ls = [int(e) for e in fileinput.input()]
    for i in xrange(1, ls[0] + 1):
        n= int(ls[i])   # read a list of integers, 2 in this case
        dic = []
        for k in xrange(1, 10000):
            if k*n==(k-1)*n:
                break
            if testNum(k*n,dic) == 10:
                print "Case #{}: {}".format(i,  k*n)
                break
        if testNum(k*n,dic)!=10:
            print "Case #{}: {}".format(i,  'INSOMNIA')
#        print "Case #{}: {} {}".format(i, n )
            