'''
@author: Kamil
'''
from math import sqrt

def isPrime(n):
    if n <= 3:
        return (True, -1)
    for i in range(2, int(sqrt(n) + 1)):
        j = int(n / i)
        if i*j == n:
            return (False, i)        
    return (True, -1)    
  
def addOne(l):
    acc = 1
    i = 0
    while True:
        l[i] = l[i] + acc
        if l[i] == 1:
            acc = 0
        else:
            l[i] = 0
            if i == len(l) - 1:
                l.append(0)
        if acc == 0:
            break;
        i = i + 1
    return l

def jamcoinValue(jamcoin, base):
    s = 0
    k = 1
    for c in jamcoin:
        s = s + c*k
        k = k*base
    return s

def findPrime(N, J):
    jamcoin = [1]
    
def smallestJamcoin(size):
    l = [0]*size
    l[0] = 1
    l[size - 1] = 1
    return l
    
def isPrimeInEveryBase(jamcoin):
    divisors = []
    for i in range(2, 11):
        primalityResult = isPrime(jamcoinValue(jamcoin, i))
        divisors.append(primalityResult[1])
        if primalityResult[0]:
            return (False, divisors)
    return (True, divisors)
     
def getJamcoins(length, n):
    l = smallestJamcoin(length)
    result = []
    while len(l) == length:
        l = addOne(l)
        l = addOne(l)
        temp = isPrimeInEveryBase(l)
        if (temp[0]):
            result.append((list(l), temp[1]))
        if (len(result) == n):
            break
    return result

results = getJamcoins(16, 50)
print("Case #1:")
for r in results:
    r[0].reverse()
    print((''.join(str(x) for x in r[0]))  + " " + str(r[1][0]) + " " + str(r[1][1]) + " " + str(r[1][2]) + " " + str(r[1][3]) + " " + str(r[1][4]) + " " + str(r[1][5]) + " " + str(r[1][6]) + " " + str(r[1][7]) + " " + str(r[1][8]))
    
# a = jamcoinValue([1, 0, 1, 1, 0, 1], 2)
# print(a)
# a = jamcoinValue([1, 0, 1, 1, 0, 1], 3)
# print(a)
# a = jamcoinValue([1, 0, 1, 1, 0, 1], 4)
# print(a)
# a = jamcoinValue([1, 0, 1, 1, 0, 1], 5)
# print(a)
# a = jamcoinValue([1, 0, 1, 1, 0, 1], 6)
# print(a)
# a = jamcoinValue([1, 0, 1, 1, 0, 1], 7)
# print(a)
# a = jamcoinValue([1, 0, 1, 1, 0, 1], 8)
# print(a)
# a = jamcoinValue([1, 0, 1, 1, 0, 1], 9)
# print(a)

    
     
# f = open('output.txt','w')
#   
# with open('B-large.in') as file:
#     lines = file.readlines()
#     for i in range(0, len(lines)):
#         n = lines[i]
#         print("Case #" + str(i) + ": " + str(task2(n)))
# #         print("Case #" + str(i) + ": " + task1(n), file = f)
#           

            
    