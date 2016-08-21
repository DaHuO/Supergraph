#!/usr/bin/env python

import sys
soln = []

def fractiles(k,c,s):
    global soln
    soln[:] = []
    if(c==1):
        if(k<=s):
            for i in range(1,k+1):
                soln.append(i)
    elif k==1:
        soln.append(k)
    else:
        pos=0
        ind=0;
        while(pos<k**c):
            pos=0
            cnew=c-1
            while(cnew>0):
                pos+=ind*(k**cnew)
                cnew-=1
            pos = pos+2+ind
            if pos>k**c:
                if pos-1<=k**c:
                    soln.append(pos-1)
            else:
                soln.append(pos)
            ind+=2
    if len(soln)>s:
        soln[:] = []

def main():
    global soln
    data=[]
    fp = open(sys.argv[1])
    t0=1
    for line in fp:
        d = line.split()
        data.append(d);
    t = int(data[0][0]);
    i=1;
    while t>0:
        t-=1
        fractiles(int(data[i][0]),int(data[i][1]),int(data[i][2]))
        i+=1
        if len(soln)>0:
            print 'Case #%d:'%(t0),' '.join(str(e) for e in soln)
        else:
            print 'Case #%d: IMPOSSIBLE'%(t0)
        t0+=1
        
        
 
if __name__ == '__main__':
    main()