#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sahil
#
# Created:     09-04-2016
# Copyright:   (c) sahil 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import fileinput
f=fileinput.input()

t= int(f.readline())
#int(raw_input())
s=t+1
while(t!=0):
    n=int(f.readline())
    if(n==0):
        print "Case #{}: INSOMNIA".format(s-t)
        t-=1
        continue

    a=[1,2,3,4,5,6,7,8,9,0]
    i=1
    while(len(a)>0):
        m=n*i
        rslt=m
        while(m!=0):
            digit=m%10
            m=m/10
            try:
                a.remove(digit)
            except ValueError:
                error=1

        i+=1

    print "Case #{}: {}".format(s-t,rslt)
    t-=1


