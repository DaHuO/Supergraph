from math import sqrt
import itertools as it


def interpretInBase10(numString, base):
    strLen = len(numString)
    return sum( int(numString[i]) * (base**(strLen-i-1)) for i in range(strLen) )

def findDivisor(N):
    if N%2 == 0:
        return str(2)
    for i in range(3,min(102,int(sqrt(N)+1)),2):
        if N%i == 0:
            return str(i)
    return None

def findJamcoins(N,J):
    jamcoins = []
    insideJamGenerator = it.product('01', repeat = N-2)
    for inside in insideJamGenerator:
        badNum = False
        num = '1' + "".join(inside) + '1'
        candidate = ['1' + "".join(inside) + '1']
        for base in range(2,11):
            inBase = interpretInBase10(num, base)
            div = findDivisor(inBase)
            if div is None:
                badNum = True
                break
            candidate.append(div)
        if badNum:
            continue
#        if any(i is None for i in candidate):
#            continue
        jamcoins.append(" ".join(candidate))
        if len(jamcoins) == J:
            return jamcoins

def main():
    T = int(raw_input())
    N, J = [int(s) for s in raw_input().split(" ")]
    for i in range(1, T+1):
        print "Case #1:"
        jamcoins = findJamcoins(N, J)
        for s in jamcoins:
            print s

if __name__ == "__main__":
    main()
    #print interpretInBase10('100001', 4)


