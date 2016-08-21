#! /usr/bin/python

import sys
import math

if len(sys.argv) < 2:
	exit(1)

finname = sys.argv[1]
foutname = finname.replace(".in",".out")

print "{} {}".format(finname,foutname)

fin=open(finname,"r")
fout=open(foutname,"w")

numcases=int(fin.readline());

print numcases


def inList(elem, lst):
    try:
        i=lst.index(elem)
        return True
    except:
        return False


def Find1st(lst):
    if inList('Z',lst):
        lst.remove('Z')
        lst.remove('E')
        lst.remove('R')
        lst.remove('O')
        result.append(0)
        return True
    if inList('W',lst):
        lst.remove('T')
        lst.remove('W')
        lst.remove('O')
        result.append(2)
        return True
    if inList('X',lst):
        lst.remove('S')
        lst.remove('I')
        lst.remove('X')
        result.append(6)
        return True
    if inList('G',lst):
        lst.remove('E')
        lst.remove('I')
        lst.remove('G')
        lst.remove('H')
        lst.remove('T')
        result.append(8)
        return True
    return False

def Find2nd(lst):
    if inList('T',lst):
        lst.remove('T')
        lst.remove('H')
        lst.remove('R')
        lst.remove('E')
        lst.remove('E')
        result.append(3)
        return True
    if inList('S',lst):
        lst.remove('S')
        lst.remove('E')
        lst.remove('V')
        lst.remove('E')
        lst.remove('N')
        result.append(7)
        return True
    return False

def Find3rd(lst):
    if inList('R',lst):
        lst.remove('F')
        lst.remove('O')
        lst.remove('U')
        lst.remove('R')
        result.append(4)
        return True
    if inList('O',lst):
        lst.remove('O')
        lst.remove('N')
        lst.remove('E')
        result.append(1)
        return True
    if inList('F',lst):
        lst.remove('F')
        lst.remove('I')
        lst.remove('V')
        lst.remove('E')
        result.append(5)
        return True
    return False

def FindFin(lst):
    while len(lst)>0:
        lst.remove('N')
        lst.remove('I')
        lst.remove('N')
        lst.remove('E')
        result.append(9)
    
    
    

for case in range(0,numcases):
    fout.write ("Case #%d: " % (case+1))
    inStr=fin.readline().strip()
    numList=list(inStr)
    result=list()
    print "num: %s" % str(numList)
    #i=inList('X',numList);
    #print i
    more=True
    while more:
        more=Find1st(numList)
    more=True
    while more:
        more=Find2nd(numList)
    more=True
    while more:
        more=Find3rd(numList)
    FindFin(numList)
    result.sort()
    resStr=''.join(str(i) for i in result)

    print resStr
    fout.write("%s\n" % resStr)
       



    #outStr=inStr[0];
    #for i in range(1,len(inStr)):
    #    if inStr[i]>=outStr[0]:
    #        outStr=inStr[i]+outStr
    #    else:
    #        outStr=outStr+inStr[i]
    #print "outStr: %s" % outStr
    #fout.write ("%s\n" % outStr)
            


#    r=int(line.pop(0))
#    c=int(line.pop(0))
#    w=int(line.pop(0))

#    print "r: %d, w: %d, c: %d" % (r,w,c)

#    if (c == w):
#        print "sol: %d" % (w)
#        sol=w
#    else:
#        div=int(c/w)
#        if(0 == c%w):
#            div=div-1
#        sol=div+w
#        print "sol: %d" % (sol)
#    fout.write ("%d\n" % (sol))

#	print "%d %d" % (sum1, sum2)
#	fout.write("%d %d\n" % (sum1, sum2) )
			



