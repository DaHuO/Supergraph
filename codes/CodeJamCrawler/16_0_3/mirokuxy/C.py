
import math


N = 32 
J = 500

s = ""
nums = [0] * 11
divisors = [0] * 11

def generateNums():
    s = bin(nums[2])[2:]
    
    #print s

    for i in range(3,11):
        nums[i] = int(s, i)

    #print nums    

def init():
    nums[2] = (2 ** (N-1)) + 1
    generateNums()

def findDivisor(n):
    if n <= 1:  return 1
    if n % 2 == 0: return 2

    half = int(math.sqrt(n) + 0.5)
    for i in xrange(3, half, 2):
        if n % i == 0: return i

    return 1

def tryNums():
    for i in range(2,11):
        divisor = findDivisor(nums[i])
        if divisor == 1: 
            return False
        else:
            divisors[i] = divisor

    return True

def increment():
    nums[2] += 2
    generateNums()

def find():
    init()

    count = 0
    while count < J:
        if(tryNums()):
            count += 1

            """
            print nums[10],
            for i in range(2,11):
                print '{0:6d} '.format(nums[i]),
            print
            """

            print nums[10],
            for i in range(2,11):
                #print '{0:6d} '.format(divisors[i]),
                print divisors[i],
            print

        increment()


if __name__ == '__main__':
    print 'Case #1:'
    find()













