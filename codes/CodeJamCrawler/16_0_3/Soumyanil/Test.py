import itertools
def toBinary(num):
    pos,res=1,0
    while num>0:
        res=res+((num%2)*pos)
        pos=pos*10;
        num=num/2
    return res
def checkJamCoin(snum):
    if snum[0]=='1' and snum[len(snum)-1]=='1':
        return 1
    return 0
def mrange(start, stop, step):
    while start < stop:
        yield start
        start += step

# benchmarked on an old single-core system with 2GB RAM.

from math import sqrt

def is_prime(num):
    if num == 2:
        return True
    if (num < 2) or (num % 2 == 0):
        return False
    return all(num % i for i in mrange(3, int(sqrt(num)) + 1, 2))
def convertBase(snum,base):
    power=len(snum)
    p=power
    res=0
    for i in range(0,power):
        res=res+(int(snum[i])*pow(base,p-1))
        p=p-1
    return res
def checkDivisor(num):
    for i in mrange(2,num,1):
        if num%i==0:
            return i
    return 0
count,flag=0,1
l=[]
print "Case #1:","\n"
for i in range(32769,pow(2,16)):
    binaryNum=toBinary(i) 
    if(checkJamCoin(str(binaryNum))==1):
        flag=1
        for j in range(2,11):
            forPrime=convertBase(str(binaryNum),j)
            #print count+1,":",binaryNum,":",forPrime
            if(is_prime(forPrime)==True):
                flag=0
                break
        if(flag==1):
           #print count+1,":",binaryNum
            for j in range(2,11):
                flag1=1
                forDivisor=convertBase(str(binaryNum),j)
                if(checkDivisor(forDivisor)==0):
                    flag1=0
                    break
            if(flag1==1):
                print binaryNum,
                for j in range(2,11):
                    forDivisor=convertBase(str(binaryNum),j)
                    print checkDivisor(forDivisor),
                print "\n"
                count=count+1                   
    if(count==50):
        break
#print l

