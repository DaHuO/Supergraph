fin = open('A-large.in')
fout = open('output.txt', 'w')
T = int(fin.readline())
for test in range(T):
    fout.write('Case #{0}: '.format(test + 1))

    val = int(fin.readline())
    if val == 0:
        fout.write('INSOMNIA\n')
    else:
        s = set()
        n = 0
        while len(s) < 10:
            n += val
            for d in str(n):
                s.add(d)
        fout.write(str(n) + '\n')

