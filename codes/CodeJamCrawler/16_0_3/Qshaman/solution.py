from math import sqrt

def isPrime(x):
    for i in xrange(2, int(sqrt(x) + 1e-9)):
        if x % i == 0:
            return i
    return False

def sol():
    N, J =  16, 50
    re = []
    for i in range(2 ** (N-2)):
        x = '1{:014b}1'.format(i)
        divisors = []
        for base in range(2,11):
            y = int(x, base)
            divisor = isPrime(y)
            if divisor:
                divisors.append(divisor)
            else:
                break
        if len(divisors) == 9:
            re.append((x, divisors))
        if len(re) == J:
            break

    return re

print 'Case #1:'
result = sol()
for num in result:
    print '{0} {1}'.format(num[0], ' '.join([str(x) for x in num[1]]))
