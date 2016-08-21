

OPPOSITE = {
        '-': '+',
        '+': '-'
        }

def pancakes(s):
    if s == '+':
        return 0
    if s == '-':
        return 1
    else:
        first = s[0]
        change_idx = s.find(OPPOSITE[first])
        if change_idx != -1:
            return 1 + pancakes(s[change_idx:])
        else:
            return pancakes(first)

with open('B-large.in') as f:
    N = int(f.readline().strip())
    for i in xrange(N):
        s = f.readline().strip()
        print 'Case #%d: %d' % (i + 1, pancakes(s))
