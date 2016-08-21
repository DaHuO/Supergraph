#!/usr/bin/python
import sys
from sets import Set
import itertools

ifile=sys.argv[1]
lines=open(ifile).read().split("\n")
tc=lines[0]
lines=lines[1:]
case=1


debugLevel=0


def debug(lvl,msg):
    if debugLevel >= lvl:
        print(str(msg))


def getL(item):
    return - item.count('L')

def getPossibles(tiles, complex):
    x=Set()
    poss=[]
    for i in itertools.combinations('LG'*tiles,tiles):
        x.add(''.join(i))
    for s in x:
        ss=s
        for l in range(complex-1):
            ss=ss.replace('G','G'*tiles).replace('L',s)
        poss.append([b for b in ss])
    poss=sorted(poss, key=getL)
    debug(1,poss)
    return poss





def getMatches(items, col, val):
    sames=[]
    for item in items:
        if len(item)>col and item[col]==val:
            sames.append(item)

    if sames == []:
        return items
    return sames



def canDo(items, tries):
    debug(1,'canDo: '+str(items))
    for item in items:
        cols=range(len(item))
        for z in cols:
            pool=list(items)
            picks=[]
            t=tries
            for col in cols:
                ss=len(pool)
                pool=getMatches(pool, col, item[col])
                if len(pool) != ss:
                    t-=1
                    picks+=[col+1]
                if t <=0:
                    break

            debug(1, 'pool :'+str(pool))
            if len(pool) == 1:
                return [str(p) for p in picks]
            l=cols.pop(0)
            cols=cols+[l]
      
    return False






def process(line):
    k,c,s=line.split(' ')
    
    #poss=getPossibles(int(k),int(c))
    #x=canDo(poss,int(s))
    size=min(int(k)**int(c),int(s))
    cols=int(k)**int(c)
    step=cols/size
    z=range(1,cols+1,step)
    x=[str(y) for y in z]
    if x:
        return ' '.join(x)
    else:
        return 'IMPOSSIBLE'






while lines != [] and lines != ['']:
        line=lines[0]
        output=process(line)
	print("Case #"+str(case)+": "+output)
	lines=lines[1:]
	case+=1
	
	
