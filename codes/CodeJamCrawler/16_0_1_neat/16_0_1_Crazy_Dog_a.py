def calc(p):
    return set(list(str(p)))
ans = {}
for i in range(1, 1100000):
    ok = set()
    j = 0
    while len(ok) < 10:
        j = j + 1
        ok = ok | (calc(j * i))
    ans[i] = i * j
ans[0] = 'INSOMNIA'
f = open('A-large.in', 'U')
fout = open('hahaha.txt', 'w')
i = 0
for line in f:
    if i == 0:
        i = i + 1
        continue
    result = ans[int(line.strip())]
    fout.write('Case #%s: %s\n' % (str(i), str(result)))
    i=i+1
fout.close()
f.close()
