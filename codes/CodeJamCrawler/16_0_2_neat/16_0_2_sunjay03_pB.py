from sys import stdin
from itertools import count, imap

test_cases = int(raw_input())

def flip(pancake):
    return '+' if pancake == '-' else '-'

for i, stack in enumerate(imap(list, imap(str.strip, stdin))):
    print "Case #%d:"%(i + 1),

    flips = 0
    while any(x == '-' for x in stack):
        previous = None
        for i, pancake in enumerate(stack):
            if previous is None or pancake == previous:
                stack[i] = flip(pancake)
            else:
                break
            previous = pancake

        flips += 1

    print flips
