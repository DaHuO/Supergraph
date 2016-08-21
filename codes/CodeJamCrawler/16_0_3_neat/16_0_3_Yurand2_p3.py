import concurrent.futures
import os

NUM_THREADS = 1
def compute():
    n = int(raw_input())
    lines = [raw_input() for _ in xrange(n)]

    with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
        futures = [executor.submit(algorithm, line) for line in lines]
        concurrent.futures.wait(futures)        
        for i, future in enumerate(futures, 1):
            print "Case #%d: %s" % (i, future.result())

def toStr(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]

def find_divisor(n):
    '''check if integer n is a prime'''

    # all other even numbers are not primes
    if not n & 1: 
        return 2

    # range starts with 3 and only needs to go up 
    # the square root of n for all odd numbers
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return x

    return None

def algorithm(line):
    N, J = line.split()
    N = int(N)
    J = int(J)

    formatstr = "1%" + str(N-2) + "s1"
    jamcoins = []
    for i in xrange(int("1"*(N-2),2)):
        candidate = (formatstr % toStr(i, 2)).replace(" ", "0")
        representations = [int(candidate, 2), int(candidate, 3), int(candidate, 4), int(candidate, 5), int(candidate, 6), int(candidate, 7), int(candidate, 8), int(candidate, 9), int(candidate, 10),]
        jamcoin = [int(candidate, 10), ] + [find_divisor(x) for x in representations]
        if None not in jamcoin:
            jamcoins.append(jamcoin)
            if len(jamcoins) == J:
                break
    out = []
    for jamcoin in jamcoins:
        out.append("\n" + " ".join([str(x) for x in jamcoin]))
    return "".join(out)

compute()
