from time import sleep

def single(func):
    return func(raw_input())

def printcase(case, out, pattern='Case #%d: %s'):
    print pattern % (case, out)

def flip(stack):
    return ''.join('-' if c == '+' else '+' for c in reversed(stack))

def solve(stack):
    flips = 0
    hi_sad = stack.find('-')
    if hi_sad >= 0:
        stack = '-'*hi_sad + stack[hi_sad:]
        flips += (hi_sad > 0)
        lo_sad = stack.rfind('-')
        flips += 1 + solve(flip(stack[:lo_sad + 1]))
    return flips

T = single(int)
for t in xrange(1, T + 1):
    stack = single(str)
    printcase(t, solve(stack))

