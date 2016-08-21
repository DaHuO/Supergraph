
def solve(s):
    if len(set(s)) == 1:
        if '+' in set(s):
            return 0
        else:
            return 1
    first = s[0]
    for i in range(1, len(s)):
        if first != s[i]:
            return 1 + solve(s[i:])

fname = 'test.txt'
fname = 'B-small-attempt0.in'
fname = 'B-large.in'
fin = open(fname)
lines = fin.readlines()
fin.close()

for k, line in enumerate(lines[1:]):
    print('Case #%d: %d' % (k+1, + solve(line.strip())))
