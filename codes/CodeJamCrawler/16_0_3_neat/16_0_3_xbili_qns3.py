import os, sys
import math

def is_not_base_prime(num):
    for j in xrange(2, 11):
        if is_prime(int(num, j)):
            return False
    return True

def is_prime(n):
    if n < 2:
        return False
    for i in xrange(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# n: length of jamcoin
# takes in a hashset to check if jamcoin has been generated before
def generate_jamcoin(n, hs):
    max_num = 2 ** (n-2) - 1

    for i in xrange(0, max_num):
        num = '1' + format(i, '0%sb' % str(n-2)) + '1'
        if num in hs:
            continue
        hs.add(num)

        if is_not_base_prime(num):
            return num

def find_factor(n):
    for i in xrange(2, n + 1):
        if n % i == 0:
            return i

def generate_divisors(n):
    res = ''
    for i in xrange(2, 11):
        factor = find_factor(int(bin(n)[2:], i))
        res += ' ' + str(factor)
    return res


if __name__ == '__main__':
    out = open(sys.argv[2], 'w')
    f = open(sys.argv[1])
    testcases = f.readline()

    for i in xrange(1, int(testcases)+1):
        inpt = map(int, str(f.readline().strip()).split(' '))
        n = inpt[0]
        res = "Case #{i}:\n".format(i=i)
        jc_hs = set()
        for k in xrange(0, int(inpt[1])):
            jamcoin = generate_jamcoin(n, jc_hs)
            res += jamcoin
            res += generate_divisors(int(jamcoin, 2))
            res += '\n'
        out.write(res)
