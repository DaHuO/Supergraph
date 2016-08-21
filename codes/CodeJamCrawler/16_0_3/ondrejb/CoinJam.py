import itertools
import math

def giveNumTen(num, base):
    ans = 1 + base**15
    for e in range(0,14):
        ans = ans + int(str(num)[e])*(base**(14-e))
    return ans
    
def primeDiv(num):
    # if it is prime, return -1, else a divisor
    if num == 2:
        return -1
    if num % 2 == 0 or num <= 1:
        return 2

    sqr = int(math.sqrt(num)) + 1

    for divisor in range(3, sqr, 2):
        if num % divisor == 0:
            return divisor
    return -1

out = open("C:\Users\Ondrej Bohdal\Downloads\\CoinJamSmall.out","w")
out.write(("Case #1:\n"))
x = ["".join(item) for item in itertools.product("10", repeat=14)]
printed = 0
array = []
for e in x:
    array = []
    for k in [2,3,4,5,6,7,8,9,10]:
        m = primeDiv(giveNumTen(e,k))
        if primeDiv(giveNumTen(e,k)) != -1:
            array.append(m)
    if len(array) == 9:
        printed = printed + 1
        out.write("1"+str(e)+"1 "+str(array[0])+" "+str(array[1])+" "+str(array[2])+" "+str(array[3])+" "+str(array[4])+" "+str(array[5])+" "+str(array[6])+" "+str(array[7])+" "+str(array[8])+"\n")
    print printed    
    if printed == 50:
        break
out.close()        
