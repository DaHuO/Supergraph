primesLimit = 10000000
primes = []
n = 0
j = 0

def sieve():
    global primes
    isPrime = [True for i in range(0, primesLimit + 1)]
    for i in range(2, len(isPrime)):
        if isPrime[i]:
            primes.append(i)
            for j in range(i+i, primesLimit+1, i):
                isPrime[j] = False

def tryPrinting(digits):
    global n
    divisors = [0,0,0,0,0,0,0,0,0,0,0]
    for b in range(2, 11):
        val = 0
        for i in range(n-1, -1, -1):
            val = val * b + digits[i]
        sqrtVal = int(val ** .5) + 1
        for i in range(0, len(primes)):
            if primes[i] >= sqrtVal:
                break
            if val % primes[i] == 0:
                divisors[b] = primes[i]
                break
        if divisors[b] == 0:
            return False
    resultStr = ""
    for i in range(n-1, -1, -1):
        resultStr += str(digits[i])
    for b in range(2, 11):
        resultStr += " " + str(divisors[b])
    print resultStr
    return True

def recursiveGenerator(digits, val, index):
    global j
    if j > 0:
        digits[index] = val
        if index == 1:
            result = tryPrinting(digits)
            if result:
                j -= 1
        else:
            recursiveGenerator(digits, 0, index - 1)
            recursiveGenerator(digits, 1, index - 1)

def solve():
    global n
    global j
    sieve()
    T = int(raw_input())
    for t in range(1, T+1):
        inp_line = raw_input()
        n, j = [int(i) for i in inp_line.split()]
        print "Case #" + str(t) + ":"
        digits = [0] * n
        digits[0] = 1
        digits[n-1] = 1
        recursiveGenerator(digits, 0, n-2)
        recursiveGenerator(digits, 1, n-2)

if __name__ == "__main__":
        solve()
