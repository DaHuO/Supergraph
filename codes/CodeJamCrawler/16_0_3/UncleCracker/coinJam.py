'''
Created on Apr 9, 2016

@author: christoph
'''

def isPrime(num):
    if num <= 1:
        return (False, 1)
    elif num <= 3:
        return (True, -1)
    elif num % 2 == 0:
        return (False, 2)
    elif num % 3 == 0:
        return (False, 3)
    i = 5
    while i**2 < num:
        if num % i == 0:
            return (False, i)
        if num % (i+2) == 0:
            return (False, i+2)
        i += 6
    return (True, -1)

def main():  
    T = int(raw_input())
    for i in range(T):
        line = raw_input().split()
        N = int(line[0])
        J = int(line[1])
        b = bin(2**(N-1)+1).replace("0b","")
        nonDict = {}
        nonPrimes = 0
        while int(b,2) < 2**N:
            nonList = []
            for j in range(2,11):
                num = int(b,j)
                res = isPrime(num)
                if res[0]:
                    break
                else:
                    nonList.append(str(res[1]))
            else:
                nonPrimes += 1
                nonDict[b] = nonList
                if nonPrimes >= J:
                    break
            b = bin(int(b,2)+2).replace("0b","")
        print "Case #" + str(i+1) + ":"
        for k,v in nonDict.iteritems():
            print k + " " + " ".join(v)

if __name__ == "__main__":
    main()