def flip(s, i):
    sl = list(s)
    for j in xrange(i):
        sl[j] = '-' if s[i-j-1] == '+' else '+'
    return ''.join(sl)

def f(s):
    if all([c == '+' for c in s]):
        return 0
    n_leading_plus = len(s)
    n_trailing_minus = len(s)
    for i, c in enumerate(s):
        if c == '-':
            n_leading_plus = i
            break
    for i in xrange(len(s)-1,-1,-1):
        c = s[i]
        if c == '+':
            n_trailing_minus = len(s) - i - 1
            break
    if n_leading_plus > 0 and n_trailing_minus > 0:
        return 1 + f(flip(s, n_leading_plus))
    if n_trailing_minus > 0:
        return 1 + f(flip(s, len(s)))
    n_trailing_plus = len(s)
    for i in xrange(len(s)-1,-1,-1):
        c = s[i]
        if c == '-':
            n_trailing_plus = len(s) - i - 1
            break
    return f(s[:(len(s) - n_trailing_plus)])

n = int(raw_input())
for i in xrange(n):
    s = raw_input()
    print 'Case #{}: {}'.format(i+1,f(s))
