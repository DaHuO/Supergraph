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
    #print "input", args
    a=0
    #print bin(a), a
    for i in range(1,100):
        s=str((i * args))
        #print "s", s, "a:", bin(a), a
        for c in s:
            #print c
            a|=(1<<int(c))
        #print "s", s, "a:", bin(a), a
        if a == 1023:
            return i * args
        
#    print "mk", args, bin(a), a
        
    return "INSOMNIA"

for x in range(T):
	temp=i.readline()
	z=solve(rls(temp))
	wout(o, x+1, z)

