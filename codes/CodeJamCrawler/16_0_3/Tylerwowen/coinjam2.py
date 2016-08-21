import sys
import math

T = int(sys.stdin.readline())

line = sys.stdin.readline().split()
N = int(line[0])
J = int(line[1])

print("Case #1:")


def make_num(length, fill):
    num = '1'
    for i in range(1, length-1):
        num += fill
    num += '1'
    return num


def add_two(num):
    added = int(num, 2) + 8
    return str(bin(added))[2:]


def divisor(num):
    if num % 2 == 0:
        return 2
    end = math.ceil(math.sqrt(num))
    count = 0
    for di in range(3, end, 2):
        if num % di == 0:
            return di
        count += 1
        if count > 1000:
            break
    return 0

acumm = make_num(N, '0')
count = 0
while count < J:
    divisors = []

    for b in range(2, 11):
        val = int(acumm, b)
        d = divisor(val)
        if d == 0:
            break
        divisors.append(d)
        # print(b, acumm, val, d)

    if len(divisors) == 9:
        print(acumm, ' '.join(map(str, divisors)))
        count += 1

    acumm = add_two(acumm)
