import numpy
import sys

T = int(raw_input())


def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False, 1
    if n == 2:
        return True, -1
    if not n & 1:
        return False, 2
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False, x
    return True, -1


def base_n_to_10(s, n):
    res = 0
    for i in range(len(s)):
        res += int(s[i]) * n**(len(s) - i - 1)
    return res

def isjamcoin(n):
    x = numpy.base_repr(n, 2)
    if x[0] != '1' or x[-1] != '1':
        return False

    res = []
    for i in range(2, 11):
        b = base_n_to_10(x, i)
        #b = numpy.base_repr(x, i)
        prime, d = isprime(b)
        if prime:
            return False, []
        res.append(d)
    
    return True, res

for t in range(T):
    res = []
    s = raw_input()
    N, J = s.split()
    N = int(N)
    J = int(J)
    
    for i in range(2**(N-1) + 1, 2**(N), 2):
        if(len(res) >= J):
            break
        sys.stderr.write("found " + str(len(res)) + " ,progress " + str(i) + "/" + str(2**(N)) + "\n")
        binary = numpy.base_repr(i, 2)
        jamcoin, divs = isjamcoin(i)
        if jamcoin:
            res.append((binary, divs))

    
    print("Case #{0}:".format(t+1))
    for i in range(J):
        print "{} {}".format(res[i][0], ' '.join(map(str, res[i][1])))
