import sys
import itertools
import math

def smallest_divisor(num):
    i = 3
    sqrt_num = int(math.sqrt(num))
    while i <= sqrt_num and i < 100000:
        if num % 2 == 0:
            return 2
        elif num % i == 0:
            return i
        i += 2
    return num

def isprime(x):
    if x == smallest_divisor(x):
        return True
    return False
    
def decim(a, base):
    i = len(a) - 1
    j = 0
    res = 0
    while i >= 0:
        res += a[i] * pow(base, j)
        j += 1
        i -= 1
    return res

def decim_interp(a):
    bases = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(len(bases)):
        bases[i] = decim(a, bases[i])
    return bases


def is_jamcoin(a):
    bases = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    for base in bases:
        num = decim(a, base)
        if isprime(num):
            return False
    return True
    

        
def jamcoin(n, j):
    bits_list = itertools.product((0,1), repeat=n)
    jamcoin_list = []
    i = 0
    for bits in bits_list:
        if bits[0] == 1 and bits[-1] == 1 and is_jamcoin(bits):
            # print >> sys.stderr, len(jamcoin_list)
            jamcoin_list.append(bits)
            if len(jamcoin_list) >= j:
                break 
    for coin in jamcoin_list:
        print "".join(map(str, coin)),
        decim_list = decim_interp(coin)
        for num in decim_list:
            print smallest_divisor(num),
        print


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for i in range(T):
        line = sys.stdin.readline()
        para_list = line.split()
        n, j = map(int, para_list)
        print "Case #%d:" % (i + 1)
        jamcoin(n, j)