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





def bestflipspotx(cakes):
    cakes=cakes.rstrip('+')
    bestrun=0
    mostUp=0
    mostDown=0
    for i in range(1,len(cakes)+1):
        if '-'*i in cakes:
            mostDown=i
            if i > bestrun:
                bestrun=i
                bestkind='-'

        if '+'*i in cakes:
            mostUp=i
            if i > bestrun:
                bestrun=i
                bestkind='+'

    if bestkind=='-' and cakes[0]=='+':
        if mostUp == mostDown:
            bestkind='+'


    debug(3,'bestrun: '+str(bestrun))
    flipspot=cakes.index(bestkind*bestrun)+bestrun


#    if flipspot != 1:
#        if cakes[0:flipspot-bestrun]==bestrun*'+':
#            flipspot=cakes.index('+'*bestrun)+bestrun

    debug(3,'mostUp: '+str(mostUp))
    debug(3,'mostDown: '+str(mostDown))
    debug(3,'bestkind: '+bestkind)
    debug(3,'flipspot: '+str(flipspot))
    return flipspot


def bestflipspot(cakes, minus=0):
    cakes=cakes.rstrip('+')
    bestspot=len(cakes) - minus
    if cakes[0] == '+':
        bestspot=1
        for i in range(1,len(cakes)):
            if cakes[i]=='+':
                bestspot+=1
            else:
                break

    return bestspot

    

def flipAt(cakes,num):
    cand=cakes[:num][::-1]
    rest=cakes[num:]
    return cand.replace('-','_').replace('+','-').replace('_','+')+rest


def flip(cakes):
    debug(2,'preflip: '+cakes)
    num=bestflipspot(cakes)
    flipped=flipAt(cakes,num)
    if flipped == cakes:
        flipped=flipAt(cakes,num-1)

    debug(1,'postflp: '+flipped)

    return flipped

#    return safe+str(bin(int(rest,2) &~ int('1'*len(rest),2))).replace('0b','')



def process(stack):
    flips=0
    debug(1,"BEGIN:   "+stack)
    while '-' in stack:
        flips+=1
        stack=flip(stack)
        debug(2, str(flips) + ":   " + stack)


    return str(flips)






while lines != [] and lines != ['']:
        line=lines[0]
        output=process(line)
	print("Case #"+str(case)+": "+output)
	lines=lines[1:]
	case+=1
	
	
