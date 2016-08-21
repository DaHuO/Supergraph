#!/usr/bin/env python3

import sys,time, math
cin=sys.stdin
cerr=sys.stderr
cout=sys.stdout

def rl(cin):
    """readline and remove \n"""
    return cin.readline()[:-1]
cin.rl=lambda:rl(cin)
def rs(cin):
    return cin.rl().split()
cin.rs=lambda:rs(cin)
def ri(cin):
    return int(cin.rl())
cin.ri=lambda:ri(cin)
def riv(cin):
    return [int(x) for x in rs(cin)]
cin.riv=lambda:riv(cin)
def rf(cin):
    return float(cin.rl())
cin.rf=lambda:rf(cin)
def rfv(cin):
    return [float(x) for x in rs(cin)]
cin.rfv=lambda:rfv(cin)
def rev(i):
    o=[]
    for x in range(1,1+len(i)): o+=[i[-x]]
    return o
def revs(s):
    return ''.join(rev(s))
def isPrime(n):
    for i in range(2, int(math.sqrt(n))):
        if not i%n:
            return true

def printr(*args):
    cerr.write(', '.join([repr(x) for x in args])+'\n')

class bin_base:
    def __init__(self):
        pass
    def up(self):
        pass
    def lo(self):
        pass
    def cont(self):
        pass
class bin_int:
    def __init__(self, m=0, M=10):
        self.m=m-1
        self.M=M+1
        self.c=int((self.M+self.m)/2)
    def up(self):
        self.m=self.c+1
        self.c=int((self.M+self.m)/2)
        return self.c
    def lo(self):
        self.M=self.c
        self.c=int((self.m+self.M)/2)
        return self.c
    def cont(self):
        return self.m < self.M

def search(r, k, pred):
    while r.cont():
        pre=pred(r.c)
        if pre < k:
            r.up()
        else:
            r.lo()
    return r.m

def parse(cin):
    return [cin.ri(), cin.riv()]
d=[chr(ord('A')+z) for z in range(26)]
def do(l):
    n2=l[0]
    p=l[1]
    t=sum(p)
    n=[]
    b=False
    while t>0:
        printr(p)
        i=p.index(max(p))
        i2=-1
        if p[i+1:]:
            i2=p.index(max(p[i+1:]), i+1)
        if i2 != -1 and n2 - p.count(0) == 2:
            if p[i]==p[i2]:
                n+= [ d[i] + d[i2] ]
                t-=1
                p[i2] -= 1
        else:
            n += [d[i]]
        p[i] -= 1
        t -= 1
    return ' '.join(n)

def main():
    start = time.time()
    T=cin.ri()
    cerr.write("Going to process {} cases\n".format(T))
    k=0
    for Ti in range(1,T+1):
        if math.log(100*Ti/T) > k:
            cerr.write("case {}...".format(Ti))
        print("case #{0}: {1}".format(Ti, do(parse(sys.stdin))))
        if math.log(100*Ti/T) > k:
            k+=1
            cerr.write("duration {}\n".format(time.time()-start))
    cerr.write("duration {0}\n".format(time.time()-start))

if __name__=="__main__":
    main()

