# Author: Jurgen Nijland
# Date  : 9-4-2016

import sys
import math


def checkDigits(nN, digits):
    while (nN >= 1):
        digits[nN % 10] = True
        nN = math.floor(nN / 10)

    b = True
    for n in digits:
        if not n:
            b = False

    return [b, digits]

counter = 0
first = True
treshold = 10000
sys.stdin.readline()

for line in sys.stdin:
    digits = [False] * 10
    status = False
    counter += 1
    i = 0
    N = int(line)
    while (i <= treshold):
        i += 1
        nN = i * N
        [status, digits] = checkDigits(nN, digits)
        if status:
            break

    if status:
        print("Case #" + str(counter) + ": " + str(nN))
    else:
        print("Case #" + str(counter) + ": INSOMNIA")
