#!/usr/bin/python3

# Z=0, W=2, U=4, X=6, G=8,
# O=1, R=3, F=5, S=7

from collections import Counter

DIGITS = ["ZERO", "TWO", "FOUR", "SIX", "EIGHT", "ONE", "THREE", "FIVE",
          "SEVEN", "NINE"]
keys = ['Z', 'W', 'U', 'X', 'G', 'O', 'R', 'F', 'S', 'N']

NUMBERS = [0,2,4,6,8,1,3,5,7,9]

def digits(string):
    cnt = Counter(string)
    counters = [Counter(DIGITS[i]) for i in range(len(DIGITS))]
    i = 0
    nums = []
    for digit in DIGITS:
        while(cnt[keys[i]] > 0):
            cnt.subtract(counters[i])
            nums.append(NUMBERS[i])
        i += 1
    return "".join([str(x) for x in sorted(nums)])


def codejammer():
    Rounds = int(input())
    for r in range(1, Rounds + 1):
        print("Case #{}: {}".format(r, digits(input())))

if __name__ == '__main__':
    codejammer()
