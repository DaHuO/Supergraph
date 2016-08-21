#!/usr/bin/env python
import sys

def find_number(letters, mindigit):
    names = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    for i in range(mindigit, 10):
        del_letters = [l for l in names[i]]
        new_letters = letters[:]
        bad_variant = False
        for l in del_letters:
            if new_letters.count(l) < 1:
                bad_variant = True
                break
            new_letters.remove(l)
        if bad_variant:
            continue
        if not new_letters:
            return str(i)
        tail = find_number(new_letters, i)
        if tail:
            return str(i) + tail
        else:
            continue
    return None

lines = [l.strip() for l in sys.stdin.readlines()]
T = int(lines[0])
assert(T == len(lines)-1)
for i in range(1, T+1):
    S = lines[i]
    sys.stdout.write("Case #{}: {}\n".format(i, find_number(list(S), 0)))
