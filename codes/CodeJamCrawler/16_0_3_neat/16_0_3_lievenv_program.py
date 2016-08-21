import math
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
def divisorGenerator(n):
    large_divisors = []
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

def is_not_prime(pos, base):
    nb = 0
    for i in xrange(0, len(pos)):
        nb += int(int(pos[i])*math.pow(base,len(pos)-i-1))
    for d in xrange(2, min(100000,nb)):
        if (nb % d == 0):
            return d
    return False
    #divisors = list(divisorGenerator(nb))
    #if len(divisors) > 2:
    #    return divisors[1]
    #else:
    #    return False

def is_jamcoin(pos):
    res = pos
    for base in xrange(2,11):
        divisor = is_not_prime(pos, base)
        if divisor:
            res += " {}".format(divisor)
        else:
            res = False
            break
    return res

t = int(raw_input())
for case in xrange(1, t+1):
    print "Case #{}:".format(case)
    n, j = [int(p) for p in raw_input().split(" ")]
    jcs_found = []
    possibilities = []
    for i1 in xrange(0, int(math.pow(2,n-2))):
        middle = "{0:b}".format(i1)
        for i2 in xrange(0, ((n-2)-len(middle))):
            middle = "0" + middle
        curr_number = "1"+middle+"1"
        possibilities.append(curr_number)
    for pos in possibilities:
        result = is_jamcoin(pos)
        if result:
            jcs_found.append(result)
            if len(jcs_found) == j:
                for jc in jcs_found:
                    print jc
                break
    #print "{}".format(nb)
