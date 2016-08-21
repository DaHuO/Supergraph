from math import sqrt

def calculateValue(n,base):
    result = 0
    lenValue = len(n)
    power = base**(lenValue-1)
    for i in xrange(lenValue):
        result+=int(n[i])*power
        power/=base

    return result

def isPrime(n):
    if n<2:
        return [False,n]
    else:
        maxVal = min(int(sqrt(n)),300000)
        if n%2==0:
            return [False,2]
        if n%maxVal==0:
            return [False,maxVal]
        
        for i in range(3,maxVal,2):
            if n%i==0:
                return [False,i]

        return [True]

def increment(n):
    length = len(n)
    val = [int(v) for v in list(n)]
    val[length-2]+=1
    for i in xrange(length-2,0,-1):
        if val[i]>1:
            val[i-1]+=1
            val[i]=0
    result = ''
    for i in val:
        result+=str(i)
    
    return result
        

raw_input()
length,count = [int(i) for i in raw_input().split(' ')]

print 'Case #1:'

        
coin = ''
for i in xrange(length-2):
    coin+='0'
coin = '1'+coin+'1'

while count>0:
    valid = 1
    divArr = ''
    for i in xrange(2,11):
        baseVal = calculateValue(coin,i)
        divVal = isPrime(baseVal)
        
        if (divVal[0]):
            valid = 0
            break
        if i!=10:
            divArr += str(divVal[1]) + ' '
        else:
            divArr += str(divVal[1])


    result = coin + ' ' + divArr
    coin = increment(coin)
    
    if not valid:
        continue
    
    print result

    count -= 1

    
