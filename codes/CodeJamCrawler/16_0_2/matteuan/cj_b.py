def check(a):
    for i in a:
        if i == False:
            return False
    return True

def solve(a):
    if len(a) == 0 or check(a):
        return 0
    count = 1
    b = list()
    b[:] = reversed(a)
    i = b.index(False)
    while i < len(b):
        b = list(map(lambda x: not x, b[i:]))
        if check(b):
            return count
        count += 1
        i = b.index(False)


nf = input()
out = nf + ".out"
fout = open(out, 'w')
f = open(nf)
T = int(f.readline())
count = 1
for line in f:
    a = []
    for c in line:
        if c == '+':
            a.append(True)
        elif c == '-':
            a.append(False)
    
    fout.write('Case #{}: {}\n'.format(count, solve(a)))
    count += 1
fout.close()
f.close()
