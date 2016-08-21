#By Luke Baird for Google CodeJam Qualifying round 2016
#problem C - Coin Jam

#base 3 is 3^x, 3^x-1, 3^x-2...3^1, 3^0
#base 4 is 4^x, 4^x-1...4^1, 4^0
#base 7 is 7^x, 7^x-1...7^1
#int("10", 2) -> 2
#int("100011", 5) -> 100011 from base 5 to base 10
T = input()
N, J = str(input()).split()
N = int(N)
J = int(J)
#N is the length of the jamcoins
#J is the number of jamcoins
def sum_digits3(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r
#write a loop to generate 0's and 1's and increase in binary by one each time
mN = N-2
print("Case #1:")
import itertools
import math
producedJamcoins = 0
for x in map(''.join, itertools.product('01', repeat=mN)):
    #we got our incrementing jamcoins
    #try to make a jamcoin out of each
    #oh yeah, add 1 to front and back of x
    x = '1'+x+'1'
    outputValues = []
    foundPrime = False
    for v in range(2, 11):
        mValue = int(x, v)
        #now for each value less than (mValue / 2) + 1 and greater than 1, see if mValue is divisible by it
        #or see if mValue == 2
        #actually we should check to see if it's divisible by prime numbers less than (mValue/2) +1
        #we can check to see if the digits add up to nine or three

        #perhaps try the theory of squaring it and adding one. if it's not divisble by 5 and its digits don't sum to three it might work...maybe...
        """squared = math.pow(mValue, 2)
        squared += 1
        if not ((squared % 5 == 0) or (sum_digits3(mValue) % 3 == 0)):
            foundPrime = True
            outputValues = []
            break
        """
        worked = False #don't need to check numbers beyond square root
        if (sum_digits3(mValue) % 3 == 0):
            outputValues.append(3)
            continue #it worked
        for val in range(2, 100000):#round(mValue ** 0.5)
            if (mValue % val == 0):
                #val works
                outputValues.append(val)
                worked = True
                break
        if not worked:
            #we failed
            foundPrime = True
            outputValues = []
            break
    if not foundPrime:
        #print the output values and the jamcoin aka x
        mString = ''
        for y in outputValues:
            mString += str(y) + ' '
        #remove last space
        mString = mString.strip()
        print('{} {}'.format(x, mString))
        producedJamcoins += 1
        if (producedJamcoins >= J):
            break

