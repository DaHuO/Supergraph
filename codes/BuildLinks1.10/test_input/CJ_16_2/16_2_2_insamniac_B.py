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


def makePoss(score):
    maxscore=score.replace('?','9')
    poss=[]
    for candscore in range(0,int(maxscore)+1):

        valid=True
        for idx in range(len(score)):
            pad=(len(score) - len(str(candscore))) *'0'
            if score[idx] != (pad+str(candscore))[idx] and score[idx] != '?':
                valid=False
        if valid:
            poss.append(candscore)

    return poss



def makeLowestMatch(c,j):
    possC=makePoss(c)
    possJ=makePoss(j)
    mindiffs=[]
    difmap={}
    lowest=99999
    for pc in possC:
        for pj in possJ:
            dif=abs(pj - pc)
            if dif < lowest:
                lowest=dif
            if not dif in difmap.keys():
                difmap[dif]=[ [pc,pj] ]
            else:
                difmap[dif].append([pc,pj])


    remaining=difmap[lowest]
    minc=99999
    minj=99999

    for x in difmap[lowest]:
        cc=x[0]
        jj=x[1]
        if cc <= minc:
            minc=cc
            if jj <= minj:
                minj=jj
            


    padc=(len(c) - len(str(minc))) *'0'
    padj=(len(j) - len(str(minj))) *'0'
    minc=padc+str(minc)
    minj=padj+str(minj)


    
    

    return " ".join([minc,minj])



def main(c,j):
    res=makeLowestMatch(c,j)

    return res
            


while lines != [] and lines != ['']:
        line=lines[0]
        [c,j]=line.split(' ')
        output=main(c,j)
	print("Case #"+str(case)+": "+str(output))
	lines=lines[1:]
	case+=1
	





def trash(c,j):
    for i in range(0,len(c)):
        if c[i]=='?' and j[i] == '?':
            if int('0'+c[0:i]) == int('0'+j[0:i]):
                c=c.replace('?','0',1)
                j=j.replace('?','0',1)
            elif int('0'+c[0:i]) > int('0'+j[0:i]):
                c=c.replace('?','0',1)
                j=j.replace('?','9',1)
            else:
                c=c.replace('?','9',1)
                j=j.replace('?','0',1)

        elif c[i]=='?':
            if int('0'+c[0:i]) == int('0'+j[0:i]):
                c=c.replace('?',j[i],1)
            elif int(c[0:i]) > int(j[0:i]):
                c=c.replace('?','0',1)
            else:
                c=c.replace('?','9',1)
        
        elif j[i] == '?':
            if int('0'+c[0:i]) == int('0'+j[0:i]):
                j=j.replace('?',c[i],1)
            elif int(c[0:i]) > int(j[0:i]):
                j=j.replace('?','0',1)
            else:
                j=j.replace('?','9',1)



#    for i in range(0,len(c)):
#        if c[i] == '?':
#            c=c.replace('?',j[i],1)
#        if j[i] == '?':
#            j=j.replace('?',c[i],1)

