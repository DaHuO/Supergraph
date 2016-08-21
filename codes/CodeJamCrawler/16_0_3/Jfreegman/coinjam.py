import sys

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]

def getDivisors(coin):
    ret = []
    count = 0
    for base in xrange(2, 11):
        if count != base - 2:
            return None

        n = int(coin, base)
        for p in PRIMES:
            if n % p == 0:
                ret.append(str(p))
                count += 1
                break

    return ret if count == 9 else None

def coinjam(T):
    lines = open(T).read().split('\n')
    num = int(lines[0])

    for i in xrange(1, num+1):
        print "Case #" + str(i) + ":"
        line = lines[i].split()
        N, J = int(line[0]) - 1, int(line[1])
        count = 0
        for j in xrange(1, 2**((N+1)-1), 2):
            coin = str(bin(2**N+j))[2:]
            divisors = getDivisors(coin)
            if divisors:
                count += 1
                print coin + " " + " ".join(divisors)

            if count >= J:
                return

if __name__ == '__main__':
    coinjam(sys.argv[1])
