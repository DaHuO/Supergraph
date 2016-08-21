# -*- coding: utf-8 -*-
"""
Created on Fri Apr 08 23:09:21 2016

@author: dan
"""
import fileinput


def solve(x,target,index):#input
    t=x*index
    sx=str(t)
    for i in sx:
        if target.count(int(i))!=0:
            target.remove(int(i))
    if len(target)==0:
        return t
    else:
        return solve(x,target,index+1)


test=[]


line=''
#print number
for line in fileinput.input():
  #  print line
    test.append(int(line.strip()))



for i in range(1,101):
    if test[i]==0:
        print "Case #"+str(i)+": INSOMNIA"
    else:
        print "Case #"+str(i)+": "+str(solve(test[i],[0,1,2,3,4,5,6,7,8,9],1))
