import sys
lines = sys.stdin.read().splitlines()
t = int(lines[0])
cases = []
for i in range(t):
    cases.append(lines[i + 1])

def flip(s, n):
    static = s[n:]
    toflip = s[:n][::-1]
    new = ''
    for c in toflip:
        if c == '+': new += '-'
        else: new += '+'
    return new + static

def how_many_flips(p):
    stack = p
    count = 0
    while True:
        if stack.find('-') == -1: break
        if stack[0] == '+':
            i = stack.find('-')
        else:
            i = stack.find('+')
        if i == -1: i = len(stack)
        stack = flip(stack, i)
        count += 1
    return count

for i, case in enumerate(cases):
    sys.stdout.write('Case #%d: %d\n' % (i + 1, how_many_flips(case)))
