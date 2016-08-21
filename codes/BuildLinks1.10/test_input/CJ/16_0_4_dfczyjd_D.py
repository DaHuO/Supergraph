fin = open('D-small-attempt0.in', 'r')
fout = open('output.txt', 'w')
t = int(fin.readline())
for x in range(t):
    print('Case #', x + 1, ':', sep='', end=' ', file=fout)
    k, c, s = [int(y) for y in fin.readline().split()]
    print(*range(1, s + 1), file=fout)
fin.close()
fout.close()