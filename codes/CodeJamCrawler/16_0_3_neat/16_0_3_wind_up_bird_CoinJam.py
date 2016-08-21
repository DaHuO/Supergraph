from math import sqrt
from itertools import count,islice,product

primes=[2]
checkagain=[]

def checkPrime(n):
    for i in primes:
        if n%i==0:
            return i
    t=0
    for i in islice(count(2),int(sqrt(n)-1)):
        if t>100000:
            checkagain.append(n)
            return 1
        if n%i==0:
            primes.append(i)
            return i
        t+=1
    return 1

input=raw_input()
for casenumber in xrange(1,int(input)+1):
    print "Case #"+str(casenumber)+":"
    info=raw_input().split()
    n=int(info[0])
    j=int(info[1])
    bases=[2,3,4,5,6,7,8,9,10]
    coinjams=[]
    for i in product("01",repeat=n-2):
        #print i
        cbase=[]
        instr="".join([str(b) for b in list(i)])
        instr="1"+instr+"1"
        for k in bases:
            #print "k",k
            num=checkPrime(int(instr,k))
            #print "num",num
            if num==1:
                break
            else:
                cbase.append(num)
        if len(cbase)==9:
            coinjams.append([instr]+cbase[0:len(cbase)])
            #print len(coinjams)
        if len(coinjams)==j:
            for p in coinjams:
                print " ".join([str(b) for b in p])
            break