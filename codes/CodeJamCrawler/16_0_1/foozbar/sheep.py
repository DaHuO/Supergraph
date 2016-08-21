import sys

with open(sys.argv[1], 'r') as f:
    contents = f.read()

lines = contents.split('\n')

lines = lines[1:]

def digits(n):
    return [int(s) for s in str(n)]

def solve(n):
    if n == 0:
        return 'INSOMNIA'
    
    seen = set()
    num = n
    for i in xrange(1000000000):
        dig = digits(num)
        seen.update(dig)
        if len(seen) == 10:
            break
        num += n
    return num

for idx, l in enumerate(lines):
    if not l:
        continue

    out = solve(int(l))
    print 'Case #%d: %s' % (idx+1, str(out))
