import sys

sys.stdin = open('A-large.in', 'r')
sys.stdout = open('A-large.out', 'w')

for c in range(1, int(input()) + 1):

    n = int(input())
    k = 0
    digits = set()
    for i in range(1, 10000):
        digits = digits | set(str(i * n))
        if len(digits) == 10:
            k = i * n
            break

    print('Case #%s: %s' % (c, k or 'INSOMNIA'))
