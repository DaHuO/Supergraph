fin = open("Counting.in", 'r')
fout = open("Counting.out", 'w')

n = int(fin.readline())
for i in range(n):
    w = int(fin.readline())
    s = set()
    fout.write("Case #{}: ".format(i + 1))
    u = 0
    if not w:
        fout.write("INSOMNIA" + '\n')
        continue
    while (len(s) != 10):
        u += w
        for i in str(u):
            s.add(i)
    fout.write(str(u) + '\n')
fin.close()
fout.close()
    