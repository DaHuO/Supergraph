fin = open('B-large.in')
fout = open('output.txt', 'w')
T = int(fin.readline())
for test in range(T):
    fout.write('Case #{0}: '.format(test + 1))

    s = fin.readline()[:-1]
    print(s)
    dff = (1 if s[-1] == '-' else 0)
    for i in range(1, len(s)):
        if not s[i-1] == s[i]:
            dff += 1
    fout.write(str(dff) + '\n')

