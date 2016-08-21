import random
import time

def miller(n):
    s=0
    #a,y,d,x
    if(n==2):
        return 1
    if(n%2==0):
        return 0
    x=n-1
    while(x%2==0):
        s = s + 1
        x = x/2
    d=x
    #a=rand()%(n-1)
    if(n<4):
        a = 2
    else:
        a = random.randint(2, n-2)
    if(a<2):
        a=2
    y=pow(a,d,n)
    if(y!=1 and y!=n-1):
        r=1
        while(r<s and y!=n-1):
            y=pow(y,2,n)
            if(y==1):
                return 0
            r = r + 1
        if(y!=n-1):
            return 0
    return 1

def gcd(x, y):
    if(y==0):
        return x
    return gcd(y,x%y)

def rho(n):
    startTime = int(round(time.time() * 1000))
    #divisor,c,x,xx,temp
    #print "rho calculation for %", n
    if(n%2==0):
        return 2
    x=2
    c=1
    divisor=1
    xx=x
    while(divisor==1):
        x=(pow(x,2,n)+c)%n;
        xx=(pow(xx,2,n)+c)%n;
        xx=(pow(xx,2,n)+c)%n;
        temp=x-xx;
        if(temp<0):
            temp = -temp
        if(temp==0):
            c = c + 1
        else:
            divisor=gcd(temp,n)
        lapsedTime = int(round(time.time() * 1000)) - startTime
        if (lapsedTime > 500):
            raise Exception("Timed out")
    return divisor

def isPrime(x):
    i = 0
    while i < 10:
        f = miller(x)
        if f == 0:
            return 0
        i += 1
    return 1

def findFactor(x):
    if isPrime(x):
        return -1
    return rho(x)

def foundAll(bitString):
    #print "processing,,,," + bitString
    arr = []
    for i in range(2,11):
        intNum = int(bitString, i)
        factor = findFactor(intNum)
        #print "Number " + repr(intNum) + " in with base " + repr(i) + " found factor " + repr(factor)
        if factor == -1:
            return 0
        else:
            arr.append(factor)
    print bitString + " " + ' '.join(map(str, arr))
    return 1

def solve(width, num):
    found = 0
    i = 0
    while found < num:
        bitString = "1" + "{0:b}".format(i).rjust(width-2, '0') + "1"
        if len(bitString) > width:
            print "no solution found:"
            return
        try:
            if foundAll(bitString):
                found += 1
                if found == num:
                    return
        except Exception, msg:
            #print "Timed out"
			i = i
        i += 1

cases = int(raw_input())
x = 1
while cases:
    width, J = raw_input().split()
    width = int(width)
    J = int(J)
    print "Case #" + repr(x) + ":"
    solve(width, J)
    #print "------------------------------------"
    #"{0:b}".format(10).rjust(4, '0')
    x += 1
    cases -= 1
