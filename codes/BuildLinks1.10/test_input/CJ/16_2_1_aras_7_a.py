import sys
import math
sys.setrecursionlimit(10000)

T = int(raw_input())

numbers_idx = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
numbers = ["ZERO", "SIX", "SEVEN", "TWO", "EIGHT", "THREE",  "FOUR", "ONE", "FIVE" , "NINE"]

"""
IENN

SEVEN
ONE
five
nine
"""
for _test in range(1, T + 1):
    answer = []

    s = raw_input()

    count = [0] * 26

    PP, P = 0, 0

    for c in s:
        count[ord(c) - 65] += 1

    for number in numbers:
        count_n = [0] * 26

        for c in number:
            count_n[ord(c) - 65] += 1

        r = 9999**99

        for x in set(number):
            r = min(r,count[ord(x) - 65] / number.count(x))

        if r > 0:
            for dd in set(number):
                count[ord(dd)-65] -= (r * number.count(dd))
                PP += (r * number.count(dd))

            for _ in range(r):
                P += (len(number))
                answer.append(numbers_idx.index(number))

    print "Case #{}: {}".format(_test, ''.join(map(str, sorted(answer))))#," --> ", P, PP, len(s)
    if P != PP or PP != len(s): print "LA CONCHA DE LA LORA"

"""
ENFVIISEOENEENVN

Case #1: 012
Case #2: 2468
Case #3: 114
Case #4: 3
"""