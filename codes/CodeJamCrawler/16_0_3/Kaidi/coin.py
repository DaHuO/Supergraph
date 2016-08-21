from math import sqrt
from itertools import count, islice

f = open('C-small-attempt2.in', 'r')
total = f.readline()
line = f.readline()
n, j = '', line
for i in line:
    if i == ' ':
        j = j[1:]
        break
    else:
        j = j[1:]
        n += i
n = int(n)
j = int(j)

def convert(base, des, num):
    res, digit = 0, 0
    while num > 0:
        res += num % des * (base ** digit)
        num //= des
        digit += 1
    return res

def divisor(n):
    for i in range(2, (n//2 + 1)):
        if n % i == 0:
            return i

def prime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
counter = 1

start = convert(2, 10, int('1' + '0'* (n - 2) + '1'))
end = convert(2, 10, int('1' * n))
with open('C-small-attempt2.out', 'a') as w:
    w.write('Case #1:\n')
for number in range(start, end + 1, 2):
    coin = convert(10, 2, number)
    res = str(coin)
    condition = True
    for base in range(2, 11):
        inter = convert(base, 10, coin)
        if prime(inter):
            condition = False
            break
        else:
            res += ' ' + str(divisor(inter))
    if not condition:
        continue
    else:
        with open('C-small-attempt2.out', 'a') as w:
            w.write(res + '\n')
        counter += 1
        if counter > 50:
            break
