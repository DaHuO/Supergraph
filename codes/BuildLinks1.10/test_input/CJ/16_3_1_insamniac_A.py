#!/usr/bin/python
import sys
from sets import Set

ifile=sys.argv[1]
lines=open(ifile).read().split("\n")
tc=lines[0]
lines=lines[1:]
case=1

abet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def getLetter(i):
    return abet[i:i+1]

debugLevel=0
def debug(lvl,msg):
    if debugLevel >= lvl:
        print(msg)



def calc(m):
    return m

def hasMajor(l):
    m=max(l)
    if l.count(m) < 2:
        return True

    return False

def willFuckUp(lis,m):
    if m == 0:
        return True
    l=list(lis)
    maxIndex=l.index(m)
    l[maxIndex]=l[maxIndex]-1
    if hasMajor(l):
        return True

    return False

def decMax(l):
    debug(3,"decMax start: "+ str(l))
    m=max(l)
    maxIndex=l.index(m)
    l[maxIndex]=l[maxIndex]-1
    r=getLetter(maxIndex)

    debug(3,"decMax2: "+ str(l))
    
#    newMax=max(l)
#    if newMax == m or newMax == 1:
#        maxIndex=l.index(newMax)
#        l[maxIndex]=l[maxIndex]-1
#        r+=getLetter(maxIndex)
    
#    debug(3,"decMax3: "+ str(l))

    for i in l:
        if len(r) == 1 and willFuckUp(l,i) == False:
            maxIndex=l.index(i)
            l[maxIndex]=l[maxIndex]-1
            r+=getLetter(maxIndex)
            break 
    
    debug(3,"decMax4: "+ str(l))

#    debug(1,[r,l])
    return [r,l]

def main(inp):
    res=[int(i) for i in inp.split(" ")]
    debug(1,res)
    o=[]
    while max(res) != 0:
        [os,res]=decMax(res)
#        debug(1,[os,res])
        o.append(os)

    return o



while lines != [] and lines != ['']:
        line=lines[0]
        pcount=line
        lines=lines[1:]
        line=lines[0]
        output=" ".join(main(line))
	print("Case #"+str(case)+": "+str(output))
	lines=lines[1:]
	case+=1
	
	
