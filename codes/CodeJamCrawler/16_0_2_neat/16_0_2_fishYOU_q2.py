# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 01:44:22 2016

@author: jiang
"""

import fileinput
def count(s):
    ct=0
#    print s,"lenth",len(s)
    if len(s)>1:
        for i in range(len(s)-1):
            if s[i] != s[i+1]:
                ct+=1
#                print  's[i]=',s[i],'s[+1i]=',s[i+1],"i=",i
    if s[-1]=='-':
        ct+=1
#        print  "s=",s
#        print  's[-1]=',s[-1]
    return ct
if __name__ == "__main__" :
    ls = [str(e) for e in fileinput.input()]
    for i in xrange(1, int(ls[0]) + 1):
        s=str(ls[i])
        s=s.replace("\n","")
        s=s.replace(" ","")
        print "Case #{}: {}".format(i,  count(s))
#        print "Case #{}: {} {}".format(i, n )