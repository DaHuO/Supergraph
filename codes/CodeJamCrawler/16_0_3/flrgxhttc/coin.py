import numpy as np

def numInBase(n,b):
    exp = 0
    s = 0
    for t in reversed(n):
        if t != '0':
           s += np.power(b,exp)
        exp += 1
    return s

def is_prime(n):
    if n == 2 or n == 3: return True, 0
    if n < 2 or n%2 == 0: return False, 2
    if n < 9: return True, 0
    if n%3 == 0: return False ,3 
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False,f
        if n%(f+2) == 0: return False,f+2
        f +=6
    return True,0   


def isJamcoin(seed):
    nums = []
    for i in range(9):
        nums.append(numInBase(seed,i+2))

    failed = False
    divs = []
    #print nums
    for n in nums:
        #print n
        p, d = is_prime(n)
        if p:
            failed = True
            break
        #print d
        divs.append(d)
    return not failed, divs

def findJamcoins(length, num):
    fi = open("./result", 'w+')
    nfound =0 
    coins =[]
    divs =[]
    
    for i in range(2**(length-2)):
        n = np.binary_repr(i,(length-2))
        n = "1"+n+"1"
        f,d = isJamcoin(n)
        if f:
            nfound += 1
            divs.append(d)
            coins.append(n)
        if nfound >= num:
            break

    fi.write("Case #1: \n")
    for i in range(len(coins)):
        line = coins[i]
        for d in divs[i]:
            line += " "+str(d)
        line += "\n"
        fi.write(line)
    #print coins
    #print divs

#def printJamcoins(length, num):
