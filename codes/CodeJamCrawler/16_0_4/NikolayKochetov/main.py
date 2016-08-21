fin = open('D-small-attempt0.in')
fout = open('output.txt', 'w')
T = int(fin.readline())

for test in range(T):
    fout.write('Case #{0}: '.format(test + 1))

    k, c, s = map(int, fin.readline().split())
    if c == 1:
        fout.write('IMPOSSIBLE\n' if s < k else ' '.join(map(str, range(1, k + 1))) + '\n')
    else:
        need = (k + 1) // 2
        if s < need:
            fout.write('IMPOSSIBLE\n')
        else:
            step = k ** (c - 1)
            fout.write(' '.join(map(str, (k - i + i * step for i in range(need)))) + '\n')
