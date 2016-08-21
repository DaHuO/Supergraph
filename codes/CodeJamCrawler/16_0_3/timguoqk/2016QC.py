# https://code.google.com/codejam/contest/6254486/dashboard#s=p2
import itertools
from math import sqrt

filein = open('2016QC.in', 'r')
fileout = open('2016QC.out', 'w')


def convertFromBase(num_str, base):
    ns = num_str[::-1]
    ans = 0
    for i in range(len(ns)):
        ans += int(ns[i]) * (base ** i)
    print((num_str, ans))
    return ans


def findDivisor(num):
    for i in range(2, int(sqrt(num) + 1)):
        if num % i == 0:
            return i
    return 0

T = int(filein.readline())
for t in range(T):
    fileout.write('Case #%d:\n' % (t + 1))
    N, J = map(int, filein.readline().split())
    j = 0
    divisors = [0 for _ in range(9)]
    for x in itertools.product('01', repeat=N - 2):
        # print(x)
        x = ['1'] + list(x) + ['1']
        # print(x)
        # if ''.join(x) == '100011':
        # print('hey')
        for i in range(2, 11):
            y = convertFromBase(x, i)
            # print(y)
            divisors[i - 2] = findDivisor(y)
            # print(divisors[i - 2])
            if divisors[i - 2] == 0:
                break
        if 0 not in divisors:
            # print(divisors)
            fileout.write(
                ''.join(x) + ' ' + ' '.join(map(str, divisors)) + '\n')
            j += 1
        if j == J:
            break


filein.close()
fileout.close()
