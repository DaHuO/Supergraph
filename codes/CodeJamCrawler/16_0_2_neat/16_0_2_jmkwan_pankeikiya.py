import fileinput
import itertools

def simplify(s):
    return ''.join(a for a, _ in itertools.groupby(s.rstrip('+')))

def toggle(c):
    return '+' if c == '-' else '-'

def flip(s):
    return ''.join(reversed(list(toggle(c) for c in s)))

def solve(s):
    i = 0
    s = simplify(s)
    while s:
        if s[0] == '+':
            i += 1
        s = flip(s[1:])
        s = simplify(s)
        i += 1
    return i

if __name__ == '__main__':
    for a, l in enumerate(fileinput.input()):
        if a == 0:
            continue
        print("Case #%d: %d" % (a, solve(l.strip())))
