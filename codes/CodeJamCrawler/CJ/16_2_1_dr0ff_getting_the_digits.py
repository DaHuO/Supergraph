import sys
from collections import Counter

SDIGITS =  ("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE")
DIGITS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

MAP = dict(zip(DIGITS, SDIGITS))

def solve(s):
    c = Counter(s)
    digits = []
    for D, d in [('Z', '0'), 
                 ('X', '6'), 
                 ('S', '7'), 
                 ('W', '2'), 
                 ('G', '8'),
                 ('V', '5'),
                 ('F', '4'),
                 ('O', '1'),
                 ('I', '9'),
                 ('T', '3')]:
        if D in c:
            N = c[D]
            for _ in range(N):
                digits.append(d)
                c -= Counter(MAP[d])
    return ''.join(sorted(digits))


def main():
    answer = "Case #{0}: {1}"
    test_num = int(sys.stdin.readline())
    for tnum in range(test_num):
        ans = solve(sys.stdin.readline().strip())
        print(answer.format(tnum + 1, ans))


if __name__ == '__main__':
    main()
