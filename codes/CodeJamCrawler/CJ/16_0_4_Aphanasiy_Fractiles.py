fin = open("Fractiles.in", 'r')
fout = open("Fractiles.out", 'w')

n = int(fin.readline())
for i in range(n):
    k, c, s = map(int, fin.readline().split())
    fout.write("Case #{}: ".format(i + 1))
    if k == s:
        fout.write(' '.join([str(i) for i in range(1, k + 1)]))
    else:
        fout.write("IMPOSSIBLE")
    fout.write('\n')

fin.close()
fout.close()

        
        