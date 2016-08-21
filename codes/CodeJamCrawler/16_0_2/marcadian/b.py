
def flip(c):
    if c == '+':
        return '-'
    return '+'


t = int(raw_input())
for case in xrange(t):
    s = raw_input()
    target = '+' * len(s)
    ret = 0
    length = len(s)
    while s != target:
        i = 0
        while i < len(s) and s[i] == s[0]:
            i += 1

        s = ''.join([flip(c) for c in s[:i]]) + s[i:]
        ret += 1

    print "Case #%d: %s" % (case + 1, ret)

