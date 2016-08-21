import sys


def count_flips(stack):
    flips = 0
    for cur, prev in zip(stack[1:], stack):
        if cur != prev:
            flips += 1
    if stack[-1] == '-':
        flips += 1

    return flips

data = [string.strip() for string in open(sys.argv[-1]).readlines()]

T = data[0]

for index, stack in enumerate(data[1:]):
    print 'Case #{0}: {1}'.format(
        index + 1,
        count_flips(stack)
    )
