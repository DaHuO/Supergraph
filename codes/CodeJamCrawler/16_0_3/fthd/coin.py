import math

t = int(raw_input())  # read a line with a single integer

def get_divisor(test):
    for i in xrange(2, int(math.sqrt(test))+1):
        if test % i == 0:
            return i
    return -1

def ans(n, num):
    # maxval = 10**(n-1) + (2 * 10**(n-2))
    # sieve = [-1] * maxval
    # sieve[0] = 0
    # sieve[1] = 0
    #
    # for i in xrange(2, maxval):
    #     if sieve[i] == -1:
    #         j = 2*i
    #         while j < maxval:
    #             sieve[j] = i
    #             j += i

    proof = {}
    count = 0
    for i in xrange((1 << (n-1)), 1 << n):
        binstr = bin(i)[2:]

        if binstr[-1] == '0':
            continue

        invalid = False
        arr = []
        for j in xrange(2, 11):
            test = int(binstr, j)
            div = get_divisor(test)
            if div == -1:
                invalid = True
                break
            else:
                arr.append(div)
                pass

        if not invalid:
            proof[binstr] = arr
            count += 1
            if count == num:
                break

    for k in proof:
        print k + " " + " ".join(map(str, proof[k]))



for i in xrange(1, t + 1):
    n, j = map(int, raw_input().split())
    print "Case #1:"
    ans(n, j)