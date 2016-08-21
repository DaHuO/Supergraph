# -*- coding: utf-8 -*-

from math import sqrt
import sys

primelist = set()
def find_divisor(value):

    if(value in primelist):
        return 0

    #for i in range(2, int(sqrt(value))+2):
    for i in range(2, 100000):
        if(value % i == 0):
            # print(str(value) + " can be devided by " + str(i))
            return i

    primelist.add(value)

    return 0


def as_base(bin_str, base):
    bin_bool = [(True if x == '1' else False) for x in bin_str]
    value = 0
    for i in range(len(bin_bool)):
        value *= base
        value += 1 if bin_bool[i] else 0
    return value

T = int(input())
# T must be 1
(N, J) = [int(x) for x in input().split(" ")]

print("Case #1:")

j = 0
for i in range(pow(2, N - 2)):
    candidate = pow(2, N - 1) + i * 2 + 1
    candidate_bin = bin(candidate)[2:]
    print("Checking " + candidate_bin + "...", file=sys.stderr)
    divisors = []
    for n in range(2, 11):
        value = as_base(candidate_bin, n)
        divisor = find_divisor(value)
        if divisor:
            divisors.append(divisor)
        else:
            # Invalid jamcoin!
            break
    if(len(divisors) == 9):
        # This is good coin!
        print(candidate_bin, end=" ")
        print(" ".join([str(x) for x in divisors]))
        j = j + 1
        print(str(int(j/J*1000)/10) + "% [" + str(j) + "/" + str(J) + "]", file=sys.stderr)
        if(j == J):
            break
