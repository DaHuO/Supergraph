import math
import itertools

def isprime(n):
    '''check if integer n is a prime'''

    # make sure n is a positive integer
    n = abs(int(n))

    # 0 and 1 are not primes
    if n < 2:
        return False

    # 2 is the only even prime number
    if n == 2:
        return True

    # all other even numbers are not primes
    if not n & 1:
        return False

    # range starts with 3 and only needs to go up
    # the square root of n for all odd numbers
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False

    return True


def divisorGenerator(n):
    large_divisors = []
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i == 0 and not i == 1 and not i == n:
            return i



#def convertBinBaseX(numDecimal, base):
   # coeff = 1
    #numberConvert = 0
    #while not numDecimal/base == 0:
     #   numberConvert = numberConvert + (numDecimal % base )* coeff
      #  numDecimal = int(numDecimal / base)
       # coeff = coeff*10
   # numberConvert = numberConvert + (numDecimal % base )* coeff
   #3 return numberConvert

def jamcoinchecker(N):
    jamcoin = False
    myStrN = str(N)
    deciN = int(N)
    i = 2
    if myStrN[len(myStrN)-1] == "1" and myStrN[0] == "1":
        if not isprime(deciN):
            while i < 10 and not isprime(int(str(deciN),i)):
                i += 1
            if i == 10:
                jamcoin = True
    return jamcoin

def jamcoincheckerfloat(N):
    jamcoin = False
    myStrN = str(N)
    deciN = float(N)
    i = 2
    if myStrN[len(myStrN)-1] == "1" and myStrN[0] == "1":
        if not isprime(deciN):
            while i < 10 and not isprime(float(str(deciN),i)):
                i += 1
            if i == 10:
                jamcoin = True
    return jamcoin

def generate_comp_bin(k):
    comb = []
    for subset in itertools.product('01', repeat=k):
         comb.append(int(''.join(subset)))
    return [i for i in comb if i > 10**(k-1)]


output = open("C-small-attempt1.out", "w")
with open("C-small-attempt1.in") as f:
    T = f.readline()
    T = int(T)
    y = 0
    for y in range(T):
        s = f.readlines()
        output.write("case #"+str(y+1)+" :")
        j = 2
        x = 0
        i = 0
        listNumber = list(generate_comp_bin(16))
        while i < len(listNumber) and x < 50:
            if jamcoinchecker(listNumber[i]):
                x += 1
                j = 2
                output.write("\n"+str(listNumber[i])+" ")
                while j < 11:
                    output.write(str(divisorGenerator(int(str(listNumber[i]), j)))+" ")
                    j += 1

            i += 1

