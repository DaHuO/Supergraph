import math
import itertools

def isPrime(n):
    sqt = int(math.sqrt(n))+1
    for i in range(2, sqt+1):
        if n%i==0:
            return (False, i)
    return (True,-1)

def isJamCoin(s):
    divisors = []
    
    for i in range(2,11):
        num = int(s, i)
        prime = isPrime(num)
        if prime[0]:
            return (False, [])
        else:
            divisors.append(prime[1])
    return (True, divisors)


      
n =16
j = 50

out = open("outputC.txt", "wb")
count = 0

out.write("Case #1:\n")

pmts = ["".join(seq) for seq in itertools.product("01", repeat=n-2)]
for s in pmts:
    string = "1" + s + "1"
    ans, divisors = isJamCoin(string)
    if ans:
        res = ""
        res+=string + " "
        for num in divisors:
            res+= str(num) + " "
        out.write(res+"\n")
        count+=1
    if count >= j:
        break

out.close()
