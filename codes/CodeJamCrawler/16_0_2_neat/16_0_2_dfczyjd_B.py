fin = open('B-large.in', 'r')
fout = open('output.txt', 'w')
t = int(fin.readline())
for x in range(t):
    s = fin.readline().rstrip()
    cnt = int(s[0] == '-')
    for i in range(1, len(s)):
        if s[i] == '-' and s[i - 1] == '+':
            cnt += 2
    print('Case #', x + 1, ': ', cnt, sep='', file=fout)
fin.close()
fout.close()