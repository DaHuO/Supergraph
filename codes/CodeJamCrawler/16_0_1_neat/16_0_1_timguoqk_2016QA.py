# https://code.google.com/codejam/contest/6254486/dashboard
filein = open('2016QA.in', 'r')
fileout = open('2016QA.out', 'w')

T = int(filein.readline())
for t in range(T):
    fileout.write('Case #%d: ' % (t + 1))
    N = int(filein.readline())
    if N == 0:
        fileout.write('INSOMNIA' + '\n')
        continue
    seen = set()
    for i in range(1, 500000):
        seen = seen.union(set([x for x in str(N * i)]))
        if len(seen) == 10:
            fileout.write(str(N * i) + '\n')
            break
    if len(seen) != 10:
        fileout.write('INSOMNIA' + '\n')

filein.close()
fileout.close()
