#!/usr/bin/python
import sys
from sets import Set

ifile=sys.argv[1]
lines=open(ifile).read().split("\n")
tc=lines[0]
lines=lines[1:]
case=1

debugLevel=0
def debug(lvl,msg):
    if debugLevel >= lvl:
        print(msg)

numMap={0:"ZERO",1:"ONE",2:"TWO",3:"THREE",4:"FOUR",5:"FIVE",6:"SIX",7:"SEVEN",8:"EIGHT",9:"NINE"}
uNums=[0,2,4,6,8]
dNums=[1,3,5,7,9]


def possNums(s):
    nums=[]
    for k in numMap.keys():
        doAdd=True
        for l in numMap[k]:
            if not l in s:
                doAdd=False
        if doAdd:
            nums.append(k)

    return nums

def stripOut(s,n):
    newstr=s
    for l in numMap[n]:
        orig=str(newstr)
        newstr=newstr.replace(l,"",1)
        if orig == newstr:
            return s

    return newstr


def hasUnique(nums):
    for u in uNums:
        if u in nums:
            return True

    return False


def hasDupe(nums):
    for d in dNums:
        if d in nums:
            return True

    return False

def pullNums(s):
    debug(1,"pullNums("+str(s)+")")
    found=[]
    oldS=""
    while s != "":

        poss=possNums(s)
        while hasUnique(poss):
            for u in uNums:
                    oldS=s
                    s=stripOut(s,u)
                    if s != oldS:
                        found.append(u)
            poss=possNums(s)


        while hasDupe(poss):
            for d in dNums:
                    oldS=s
                    s=stripOut(s,d)
                    if s != oldS:
                        found.append(d)
            poss=possNums(s)



#        debug(1,s)
#        debug(1,poss)
    return found

def main(inp):
    res=pullNums(inp)
    x=[str(x) for x in res]
    x.sort()
    return "".join(x)
            


while lines != [] and lines != ['']:
        line=lines[0]
        output=main(line)
	print("Case #"+str(case)+": "+str(output))
	lines=lines[1:]
	case+=1
	
	
