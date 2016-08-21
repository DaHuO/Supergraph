from __future__ import print_function
import sys
import math

def divisor(n):
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return i
    return False

def to_base(orig, base):
    result = 0
    multiplier = 1
    for d in reversed(range(len(orig))):
        if orig[d] == '1':
            result += multiplier
        multiplier *= base
    return result

# Where p is possible jamcoin
def solution(p):
    numstr = bin(p)[2:]

    divisors = [None] * 9

    divisors[0] = divisor(p)
    if not divisors[0]:
        return False

    for b in range(3, 11):
        divisors[b - 2] = divisor(to_base(numstr, b))
        if not divisors[b - 2]:
            return False

    print(numstr, *divisors)
    return True


if __name__ == '__main__':
    t = int(input())
    split = input().split(' ')
    n = int(split[0])
    j = int(split[1])

    print('Case #1:')

    # O(n)
    start = to_base('1' + '0' * (n - 2) + '1', 2)
    end = to_base('1' * n, 2)

    num = 0

    for i in range(start, end + 1, 2):
        if solution(i):
            num += 1
            print("Found {:3d}".format(num), file=sys.stderr)

            if num == j:
                break
