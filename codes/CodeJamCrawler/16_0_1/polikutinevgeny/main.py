inf = open('input.txt', 'r')
ouf = open('output.txt', 'w')
t = int(inf.readline())
for i in range(t):
    n = int(inf.readline())
    if n == 0:
        ouf.write('Case #{}: INSOMNIA\n'.format(i + 1))
        continue
    s = set()
    p = 0
    while len(s) < 10:
        p += 1
        t = str(n * p)
        for j in t:
            s.add(j)
    ouf.write('Case #{}: {}\n'.format(i + 1, n * p))
inf.close()
ouf.close()