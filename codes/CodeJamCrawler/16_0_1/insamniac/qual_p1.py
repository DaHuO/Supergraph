#!/usr/bin/python
import sys
from sets import Set

ifile=sys.argv[1]
lines=open(ifile).read().split("\n")
tc=lines[0]
lines=lines[1:]
case=1

def isAsleep(seen):
    if len(seen) == 10:
        return True
    return False


def gotosleep(numStr):
    if numStr == "0":
        return "INSOMNIA"
    seen=Set()
    for i in numStr:
        seen.add(i)
    nums=1
    num=int(numStr)
    mult=2
    while not isAsleep(seen):
        nums+=1
        for j in str(num*mult):
            seen.add(j)
        mult+=1
#        print(seen)
    return str(num*(mult-1))






while lines != [] and lines != ['']:
        line=lines[0]
        output=gotosleep(line)
	print("Case #"+str(case)+": "+output)
	lines=lines[1:]
	case+=1
	
	
