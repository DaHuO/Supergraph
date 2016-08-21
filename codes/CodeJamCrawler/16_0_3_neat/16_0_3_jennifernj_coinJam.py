def interpretAsBase(num, base) :
    number = 0
    num = str(num)
    for i in range(len(num)-1, -1, -1) :
        number += int(num[i]) * base**(len(num)-1-i)
    return number

def numberToBase(num, base) : #eg num=5, base=2, output='101'
    numStr = ""
    place=0
    while num!=0:
        value=num%(base**(place+1))
        num-=value
        numStr=str(value//(base**place))+numStr
        place+=1
    return numStr

def isPrime(num):
    upTo=int(num**(1/2))
    for i in range(2, upTo+1):
        if num%i==0:
            return False
    if num==1:
        return False
    return True

def findCoins(numDigs, numNums):
    coins=[]
    i=2**(numDigs-1)
    while len(coins)<numNums:
        l=len(coins)
        b2=numberToBase(i, 2)
        if b2[0]=='1' and b2[len(b2)-1]=='1':
            coins.append(b2)
            for j in range(2,11): #loop over bases
                if isPrime(interpretAsBase(b2,j))==True and b2 in coins:
                    #print("about to remove", b2, "because it's prime in base", j,". it is",toAnotherBase(b2,j))
                    coins.remove(b2)
        if len(coins)>l:
            print("I found one!")
        i+=1
    return coins[0:numNums]

def findJamcoinFactors(num): #num='1000111'
    factors=[]
    for base in range(2, 11):
        jamcoinInBase=interpretAsBase(num, base)
        found=False
        i=2
        while found!=True:
            if jamcoinInBase%i==0:
                factors.append(i)
                found=True
            else:
                i+=1
    return factors

coins=findCoins(16, 50)
print("Case #1:")
for coin in coins:
    string=coin+" "
    for factor in findJamcoinFactors(coin):
        string+=str(factor)+" "
    print(string)
#print(isPrime(1023))
