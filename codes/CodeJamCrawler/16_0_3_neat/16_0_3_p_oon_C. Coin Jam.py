import re
import sys
import random

pp = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977]

# Miller-Rabin
def isp(x):
    if x in pp:
        return True
    for i in pp:
        if not x%i:
            return False
    s=x-1
    t=0
    while not (s&1):
        s=s>>1
        t+=1
    for z in range(10):
        a=random.randrange(2, x - 1)
        v=pow(a,s,x)
        if v!=1:
            i=0
            while v!=(x - 1):
                if i == t-1:
                    return False
                else:
                    i=i + 1
                    v=(v**2) % x
    return True

def check(k,ina):
    for i in range(2,11):
        if(isp(int(ina,i))):
            #print(ina+' = '+str(int(ina,i))+' failed at base '+str(i))
            return False
    return True

import fractions
# pollard-brent
def fct(z):
    if z%2==0:
        return 2
    y,c,m = random.randint(1, z-1),random.randint(1, z-1),random.randint(1, z-1)
    g,r,q = 1,1,1
    cnt = 0
    while g==1:             
        x = y
        for i in range(r):
            y = ((y*y)%z+c)%z
        k = 0
        while (k<r and g==1):
            if cnt > 100000:
                sys.stderr.write('IGNORE\n')
                return -1
            ys = y
            for i in range(min(m,r-k)):
                y = ((y*y)%z+c)%z
                q = q*(abs(x-y))%z
            cnt+=min(m,r-k)
            g = fractions.gcd(q,z)
            k = k + m
        r = r*2
    if g==z:
        while True:
            ys = ((ys*ys)%z+c)%z
            g = fractions.gcd(abs(x-ys),z)
            if g>1:
                break
    if(g>=z):
        sys.stderr.write('DIE')
        sys.exit(-1)
    return g    

def calc(n,j):
    global pcz,pc3z
    pcc = int(2**(n-2))
    oo = []
    trz = {}
    while len(oo) < j:
        for i in range(1):
            inrn = random.randrange(pcc)
            if inrn in trz:
                continue
            trz[inrn] = 1
            inrn = '1'+bin(inrn)[2:].zfill(n-2)+'1'
            if check(n-2,inrn):
                ff=[]
                for i in range(2,11):
                    fx=fct(int(inrn,i))
                    if fx==-1:
                        break
                    ff+=[fx]
                else:
                    print(inrn,' '.join(str(i) for i in ff))
                    oo+=[inrn]
                    if not len(oo) % 10:
                        sys.stderr.write(str(len(oo))+'\n')
    return 

buf=[]
def scans():
    global buf
    while 1:
        while len(buf) <= 0: buf=input().replace('\n',' ').split(' ')
        o=buf.pop(0)
        if o!='': break
    return o
def scan(): return int(scans())
sys.stdin = open('input.txt')
ofg=1
if ofg:
    sys.stdout = open('output.txt','w')
for i in range(scan()):
    print('Case #%d:'%(i+1))
    calc(scan(),scan())
if ofg:
    sys.stdout.flush()
    sys.stdout.close()