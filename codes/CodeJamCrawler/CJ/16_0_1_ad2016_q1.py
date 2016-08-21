import itertools

def q1(n):
    if n == 0:
        return 'INSOMNIA'
    digits = set()
    for i in itertools.count(1):
        for c in ('%d' % (n * i)):
            digits.add(c)
        if len(digits) == 10:
            return n * i

T = int(input())
for i in range(T):
    x = int(input())
    print('Case #%s: %s' % (i + 1, q1(x)))