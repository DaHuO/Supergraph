import sys


def is_prime(n):
    #print 'N es: ', n
    i = 1
    while True:
        i += 1
        if i == n:
            return 0
        if n % i == 0 and i not in [0,1]:
            return i
        if i > 1000000:
            return 0
    return 0


def interpret(string, base):
    res = 0
    pot = len(string) - 1
    for char in string:
        res += int(char) * pow(base, pot)
        pot -= 1
    return res


def candid(n, i):
    res = bin(i).split('b')[1]
    prefix = ''.join(['0' for n in range(n - len(res))])
    return prefix + res

n_cases = int(sys.stdin.readline())

for i in range(n_cases):
    n, j = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    print ('Case #' + str(i + 1) + ":")
    count = j
    k = 0
    while count > 0:
        candidate = '1' + candid(n - 2, k) + '1'
        divisors = []
        printar = True
        for base in [2, 3, 4, 5, 6, 7, 8, 9, 10]:
            m = is_prime(interpret(candidate, base))
            if m == 0:
                k += 1
                printar = False
                break
            divisors.append(m)
        if printar:
            divisors = [str(y) for y in divisors]
            divisors = ' '.join(divisors)
            print candidate, divisors
            count -= 1
            k += 1
