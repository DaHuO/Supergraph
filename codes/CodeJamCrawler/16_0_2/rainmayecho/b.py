def g(stack):
    n = 0
    if stack == '-'*len(stack):
        return 1
    opp = {'+': '-', '-': '+'}
    while stack != '+'*len(stack):
        if stack == '-'*len(stack):
            return n + 1
        c0 = stack[0]
        for j, c in enumerate(stack):
            if c == c0:
                continue
            else:
                break
#         print stack, j, c0
        stack = opp[c0]*j + stack[j:]
        n += 1
    return n

def G(stack):
    if stack == '+'*len(stack):
        return 0
    if stack == '-'*len(stack):
        return 1
    n = 0 + int((stack[0] == '+' and stack[-1] == '-') or (stack[0] == '-' and stack[-1] == '-'))
    prev = stack[0]
    for c in stack[1:]:
        if prev == c:
            continue
        if prev == '+':
            n += 1
            prev = '-'
        else:
            n += 1
            prev = '+'
    return n



h = open('1bout.txt', 'w')

f1 = 'test.txt'
f2 = '1blarge.in'

with open(f2, 'r') as f:
    T = f.readline()
    for i, e in enumerate(f.readlines()):
        stack = e.strip('\n')
        r = G(stack)
        print 'Case #%s: %s' %(i + 1, r)
        h.write('Case #%s: %s\n' %(i + 1, r))