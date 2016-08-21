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

def truearr( arr ):
    for i in range(0,10):
        if False == arr[i]:
            return False
    return True 

for case in range(0,numcases):
    fout.write ("Case #%d: " % (case+1))
    line=fin.readline().strip()
    line=line.split()

    k=int(line.pop(0))
    c=int(line.pop(0))
    s=int(line.pop(0))

    print "k: %d,c: %d, s: %d" % (k,c,s)
    actnum=0
    count=0

    for i in range(0,s):
        fout.write("%d " % (i+1))
    fout.write("\n");
    
    #while False==truearr (numList):
    #        count+=1
    #        actnum+=num
    #        numstr=str(actnum)
    #        print "numstr: %s" % numstr
    #        for i in range(0,len(numstr)):
    #            numList[int(numstr[i])]=True
    #fout.write("%d\n" % actnum)
    #print "count: %d" % (count)


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
			



