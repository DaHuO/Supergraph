import sys


def print_ans(i, a):
    print("Case #{0}: {1}".format(i, a))

lines = sys.stdin.readlines()

for i, l in enumerate(lines[1:], start=1):
    N = int(l)

    if N == 0:
        print_ans(i, 'INSOMNIA')
        continue

    to_see = set('0123456789') - set(str(N))
    x = N
    while to_see:
        x += N
        to_see -= set(str(x))
    print_ans(i, x)
