import sys

sys.stdin = open('A-large.in', 'r')
sys.stdout = open('a-large.out', 'w')


def find_sheep(n):
    if n == 0:
        return 'INSOMNIA'
    dig = set()
    idx = 1
    while True:
        r = set([i for i in str(n * idx)])
        dig = dig | r
        if len(dig) == 10:
            break
        idx += 1
    return str(n * idx)

for t in range(int(input())):
    r = find_sheep(int(input()))
    print 'Case #%d: %s' % (t + 1, r)
