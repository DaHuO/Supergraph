filename = 'D-small-attempt0'

fi = open(filename+'.in', 'r')
fo = open(filename+'.out', 'w')
size = fi.readline()

for case, line in enumerate(fi, start=1):
    fo.write('Case #{}: '.format(case))
    (K, C, S) = line.strip().split()
    if S < K:
        fo.write('IMPOSSIBLE\n')
        continue
    num_tiles = int(K)**int(C)
    sol = []
    for i in range(int(K)):
        sol.append(num_tiles * i// int(K))

    fo.write(' '.join([str(x+1) for x in sol])+'\n')
