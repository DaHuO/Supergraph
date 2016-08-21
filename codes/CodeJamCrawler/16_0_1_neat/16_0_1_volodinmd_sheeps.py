from __future__ import print_function
__author__ = 'volodin'

import re


def solve(N):
    if int(N) == 0:
        return "INSOMNIA"
    MaxN = int(N)
    numbers = "1234567890"
    while True:
        numbers = re.sub("[{0}]".format(MaxN), '', numbers)
        if not numbers: #if numbers is empty!
            return MaxN
        MaxN += int(N)

input = open('A-large.in', 'r')
output = open('sheeps-big-out.txt', 'w')
T = input.readline()
for i in range(0, int(T)):
    answer = solve(input.readline())
    answer = "Case #{0}: {1}\n".format(i + 1, answer)
    print(answer, end='')
    output.write(answer)