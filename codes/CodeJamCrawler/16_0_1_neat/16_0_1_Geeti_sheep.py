def lastN(n):
    numSet=set([])
    s=n
    while len(numSet) < 10:
        for c in str(s):
            numSet.add(c)
        s+=n
        if s==n:
            return 'INSOMNIA'
    return str(s-n)


with open('A-large.in') as f:
    lines = f.read().splitlines()
for i in range(1,len(lines)):
    res = lastN(int(lines[i]))
    print('Case #%d: %s' % (i,res))
