import math
import itertools
import sys

def is_prime(N):
    if N == 1 or (N > 2 and N % 2 == 0):
        return False

    x = int(math.sqrt(N))
    for i in xrange(x, 1, -1):
        if N % i == 0:
            return False

    return True

        
def get_first_divisor(N):
    x = int(math.sqrt(N))

    for i in xrange(x, 1, -1):
        if N % i == 0:
            return i

    return 1


def is_jamcoin(binary_str):
    r = binary_str[::-1]
    s = 0
    each_value = []
    
    for b in range(2, 11):
        s = 0
        for i, c in enumerate(r):
            s += ((b ** i) * int(c))
        
        if is_prime(s):
            return list()

        each_value.append(s)

    return each_value 


def create_jamcoin(N, J):
   l = list(itertools.product('01', repeat = (N - 2)))
   c = 0
   for i in l:
       k = list(i)
       k.insert(0, '1')
       k.append('1')
       r = is_jamcoin(k)
       if len(r) != 0:
           sys.stdout.write(''.join(k) + ' ')
           for m in r:
               sys.stdout.write(str(get_first_divisor(m)))
               sys.stdout.write(' ')

           sys.stdout.write('\n')
           c += 1

           if c >= J:
               break


if __name__ == "__main__":
    N = raw_input().strip().split()
    for i in range(int(N[0])):
        I = raw_input().strip().split()
        print "Case #" + str(i + 1) + ":"
        create_jamcoin(int(I[0]), int(I[1]))
