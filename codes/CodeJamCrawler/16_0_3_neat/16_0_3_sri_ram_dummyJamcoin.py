from math import sqrt
from math import floor
def isprime(n):
    if n<2:
        return False
    if n==2:
        return True
    if n==3:
        return True
    prime=True
    lim=floor(sqrt(n))+1
    if n%2==0:
        return False
    if n%2==0:
        return False
    for i in range(3,lim,2):
        if n%i==0:
            prime= False
            break
    return prime
def valid(start,j):
    numb=int(start,2)     
    x=[]
    while j:
        prime=False
        baseconverts=[start]
        for i in range(2,11):
            if not isprime(int(start,i)):
                baseconverts.append(int(start,i))
            else:
                prime=True
                break
        if prime:
            while True:
                numb+=1
                start=bin(numb)[2:]
                if start[0]=='1' and start[-1]=='1':
                    break
        else:
            x.append(baseconverts)
            j-=1
            while j:
                numb+=1
                start=bin(numb)[2:]
                if start[0]=='1' and start[-1]=='1':
                    break
    return x
def generateDivisor(num):
    gen=[num[0]]
    for i in num[1:]:
        for x in range(2,i):
            if i%x==0:
                gen.append(str(x))
                break
    return gen
def jamCoin(filename):
    f=open(filename,'rU')
    g=open('coinjamsmall.out','w')
    t=f.readline()
    N,j=map(int,f.readline().split())
    start='1'+('0'*(N-2))+'1'
    validnumswithBaseconverts=valid(start,j)
    combi9=[]
    for num in validnumswithBaseconverts:
        combi9.append(generateDivisor(num))
    g.write('Case #1:\n')
    for answer in combi9:
        g.write(' '.join(answer))
        g.write('\n')
jamCoin('C-small-attempt1.in')
