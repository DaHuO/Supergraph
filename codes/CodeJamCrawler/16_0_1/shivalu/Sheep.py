__author__ = 'shiva'

def sheep(n):
    if n == 0:
        return "INSOMNIA"
    i = 0
    l = []
    f = []
    while i <= 100:
        r = True
        i += 1
        l.append(i * n)
        lst = [int(a) for a in str(i*n)]
        for s in lst:
            if s not in f:
                f.append(s)
        for h in range(10):
            if h not in f:
                r = False
                break
        if r:
            return l[-1]
    return "INSOMNIA"

with open("A-large-attempt.in") as ff:
    inp = [lin.rstrip('\n') for lin in ff]

p = 0
o = open("output_files.txt",'w')
for i in inp[1:]:
    p += 1
    print >>o, "Case #{}: {}".format(p, sheep(int(i)))