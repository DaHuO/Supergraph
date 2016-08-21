f = open('A-large.in','r').readlines()
a = []
for x in f:
    a.append(int(x.strip()))

def solve(x):
    if x == 0:
        return 'INSOMNIA'
    dg = []
    t = x
    while (1):
        for c in str(t):
            if not int(c) in dg:
                dg.append(int(c))
        if len(dg) == 10:
            return str(t)
        t = t + x

f = open('output.txt','w')
for test in range(1, a[0] + 1):
    print >> f, "Case #" + str(test) + ': ' + solve(a[test])
f.close()
