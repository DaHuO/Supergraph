from math import sqrt

def isPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False, i
    return True, n

def jamcoin(n):
    devisors = list()
    for i in range(2, 11):
        val = int(n, i)
        prime, div = isPrime(val)
        if prime:
            return None, devisors
        devisors.append(div)
    return n, devisors
_T = T = input()
_j = 0
while T > 0:
    T -= 1
    N, J = map(int, raw_input().split())
    print "Case #%d:" % (_T - T)
    _j = 0
    def printJamcoin(n, prev):
        global _j
        if _j == J:
            return
        if n + 2 == N:
            resN, resDiv = jamcoin('1'+prev+'1')
            if resN is not None:
                _j += 1
                print resN, ' '.join(map(str, resDiv))
            return
        printJamcoin(n + 1, prev + '0')
        printJamcoin(n + 1, prev + '1')
    printJamcoin(0, "")
