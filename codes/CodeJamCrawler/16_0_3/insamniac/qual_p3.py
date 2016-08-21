#!/usr/bin/python
import sys
from sets import Set
import sympy



ifile=sys.argv[1]
lines=open(ifile).read().split("\n")
tc=lines[0]
lines=lines[1:]
case=1


debugLevel=0


def debug(lvl,msg):
    if debugLevel >= lvl:
        print(msg)



def checkit(n):
    bRep=bin(n).replace('0b','')

    divs=[]
    for b in range(2,11):
        dec=int(bRep,b)
        if sympy.isprime(dec):
            return False
        divs.append(str(max(sympy.ntheory.factorint(dec).keys())))

    print(bRep+" "+" ".join(divs))
    return True



def process(size, outputs):
    finished=0
    start=int('1'+(size-2)*'0'+'1',2)
    end=int('1'+(size-2)*'1'+'1',2)

    for i in range(start,end+1,2):
        if  checkit(i):
            finished+=1
        if finished>=outputs:
            return



while lines != [] and lines != ['']:
        line=lines[0]
	print("Case #"+str(case)+":")
        [s,o]=line.split(' ')
        process(int(s),int(o))
	lines=lines[1:]
	case+=1
	
	
