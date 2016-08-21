def findGTile(K,C,S):
    if K == S:
        return [str(i*pow(K,C - 1) + 1) for i in xrange(S)]

print findGTile(2,3,2)

fin = open('inputFile.in', 'r')
fout = open('outputFile.out', 'w')
T = int(fin.readline().strip())

for t in xrange(T):
    line = fin.readline().strip()
    args = [int(arg) for arg in line.split(' ')]
    tilesToCheck = findGTile(args[0], args[1], args[2])
    fout.write('Case #'+str(t+1)+': ' + ' '.join(tilesToCheck)+'\n')

fin.close()
fout.close()
