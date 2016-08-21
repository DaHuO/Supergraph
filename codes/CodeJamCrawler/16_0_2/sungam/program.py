#!/usr/bin/env python

import sys
import string

fname=sys.argv[1]

i=open(fname,'r')
o=open(fname+'.out','w')

'''readline Split'''
def rls(i):
	out=map(int, string.split(i))
	return out[0] if len(out)==1 else out

'''Output Case#...'''
def wout(o, i, arg):
	out="Case #"+ str(i)+":"
	out+=" "+str(arg)
	#out+=" "+''.join(arg)
	#for arg in args:
	#    out+=" "+str(arg)
	out+="\n"
	o.write(out)

T=rls(i.readline())

'''The function to solve the problem'''
def solve ( args ):
    p='+'
    cnt=0
    args=args[::-1]
    #print
    #print args
    for c in args:
        #print c
        if p!=c:
            p=c
            cnt+=1
    return cnt 

for x in range(T):
	temp=i.readline()
	z=solve(temp.rstrip())
	wout(o, x+1, z)

