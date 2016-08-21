import math

T = int(raw_input())

def get_val(v, base):
    mul = 1
    result = 0
    for i in reversed(xrange(len(v))):
        result += v[i] * mul
        mul *= base

    return result

def get_divisor(num):
    for div in xrange(2, int(math.sqrt(num)) + 1 ):
        if num % div == 0:
            return div

    return None

def next_mid(v):
    j = len(v) - 1

    if v[j] == 0:
        v[j] = 1
    else:
        v[j] = 0
        j -= 1
        while v[j] == 1:
            v[j] = 0
            j -= 1

        v[j] = 1

for i in xrange(T):
    print "Case #" + str(i+1) + ":"

    N, J = list(map(int, raw_input().split()))

    mid = [0] * (N - 2)

    for j in xrange(0, J):
        while True:
            cand = [1] + mid + [1]
            divisors = []
            for base in xrange(2, 11):
                val = get_val(cand, base)
                div = get_divisor(val)
                if (div == None):
                    divisors = None
                    break
                else:
                    divisors.append(div)

            next_mid(mid)

            if divisors != None:
                print "".join(map(str, cand)), " ".join(map(str, divisors))
                break
