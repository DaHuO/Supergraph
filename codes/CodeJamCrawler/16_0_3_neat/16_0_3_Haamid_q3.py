import math
from random import randint
import datetime
import time

def firstdivisor(n, t):
    myset = []
    limit = int(math.sqrt(n))+1
    for i in xrange(1, limit):
        now = datetime.datetime.now()
        if ((now-t).total_seconds())>0.001:
            return "Time Up"
        if n%i==0:
            myset.append(i)
            if i*i!=n:
                myset.append(n/i)
        if len(myset)>2:
            return myset[2]
            # for el in myset:
            #     if el!=2 and el!=1:
            #         return el
            #     else:
            #         continue
    return 0
# print firstdivisor(12)

# print int("1001", 4)

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n /= b
    copy = digits[::-1]
    length = len(copy)
    to_return = ""
    for i in range(length):
        to_return = to_return + str(copy[i])
    return int(to_return)

def is_prime(n, t):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        now = datetime.datetime.now()
        if ((now-t).total_seconds())>0.001:
            return "Time Up"
        if n%f == 0:
            return False
        if n%(f+2) == 0:
            return False
        f +=6
    return True

def PrimeInAnyBase(str):
    for base in xrange(2,11):
        a = datetime.datetime.now()
        result = is_prime( int(str,base),a )
        if result==True:
            return True
        elif result=="Time Up":
            return False
    return False

# print numberToBase(int("1010100101111011"),10)

# print int("111001",2)
# print int("111001",3)
# print int("111001",4)
# print int("111001",5)
# print int("111001",6)
# print int("111001",7)
# print int("111001",8)
# print int("111001",9)
# print int("111001",10)

# a = datetime.datetime.now()
# time.sleep(1)
# b = datetime.datetime.now()
# print (b-a).total_seconds()

# print (str(0))=="0"

ifile = open('input.txt','r')
ofile = open('output.txt','w')

ofile.write("Case #1:\n")

T = int(ifile.readline())
line = (ifile.readline()).split(" ")
N = line[0]
J = line[1]
setofJamCoins = set()

while len(setofJamCoins)!=int(J):
    number = "1"
    for j in range(int(N)-2):
        number = number + str(randint(0,1))
    number = number + "1"
    # print "Before PrimeInAnyBase"
    if PrimeInAnyBase(number)==True or PrimeInAnyBase(number)=="Time Up":
        print "Time Up"
        continue
    to_write = ""

    # now i know that the actual_number IS a jamcoin
    if number in setofJamCoins:
        continue

    actual_number = int(number)
    # print "actual_number: ",actual_number
    to_write = (number+" ")
    # print "Actual Number:", number

    skip = False
    for base in xrange(2, 11):
        number_in_base = int(number, base)
        # print "Before firstdivisor"
        a = datetime.datetime.now()
        result = (firstdivisor(number_in_base, a))
        if result!="Time Up" and result!=0:
            to_write = to_write + str(result) + " "
        else:
            print "Time Up"
            skip = True
            break
    if skip:
        continue
    else:
        print "Successfully Written"
        setofJamCoins.add(number)
        ofile.write(to_write+"\n")
        
ifile.close()
ofile.close()