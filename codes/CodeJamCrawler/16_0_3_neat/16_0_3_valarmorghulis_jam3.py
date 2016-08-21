f = open("C:\Users\Himan\Desktop\Downloads\C-small-attempt1.in","r")
other = open("C:\Users\Himan\Desktop\output3.txt","w")
import math
def checkPrime(num):
    half = int(math.sqrt(num))
    if num%2==0:
        if num==2:
            return (2,1)
        else:
            return (2,0)
    else:
        for i in xrange(3,half+1,2):
            if num%i==0:
                return (i,0)
            
        return (num,1)
    


def generatePrime(l,count):
    newL=[]
    p = len(l)
    for i in xrange(p):
            newL.append(l[i]+'0')
            newL.append(l[i]+'1')
    count+=1
    if count==16:
        p = len(newL)
        for i in xrange(p):
            newL[i]=newL[i]+'1'
        return newL
    else:
        return generatePrime(newL,count)
    
t = int(f.readline())

n,m=map(int,f.readline().strip().split())

l=['1']

primeList = generatePrime(l,2)

ans = []

for element in primeList:
    nonPrimeInAllBase = 0
    divisors = []
    for i in xrange(2,11):
        num = int(element,i)
        x = checkPrime(num)
        if x[1]==0:
            nonPrimeInAllBase+=1
            divisors.append(x[0])
    if nonPrimeInAllBase==9:
        ans.append([element]+divisors)
    if len(ans)==50:
        break

other.write("Case #1:\n")
for item in ans:
    for i in item:
        other.write(str(i)+" ")
    other.write("\n")


other.close()
f.close()
    

