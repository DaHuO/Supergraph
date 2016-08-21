def howManyFlips(S):
    flipsNO = 0
    S = tripStack(S)
    while len(S) > 1:
        S[0] = ['-','+'] [S[0]=='-']
        flipsNO += 1
        S = tripStack(S)
    if S[0] == '+':
        return flipsNO
    else:
        return flipsNO + 1
def tripStack(S):
    if not S:
        return S
    if len(S) == 1:
        return S
    trimed = [S[0]]
    for i in xrange(len(S)):
        if S[i] != trimed[len(trimed) - 1]:
            trimed.append(S[i])
    return trimed
    
#print howManyFlips([s for s in '--+-'])

fin = open('inputFile.in', 'r')
fout = open('outputFile.out', 'w')
T = int(fin.readline().strip())

for t in xrange(T):
    line = fin.readline().strip()
    S = line
    minNum = howManyFlips([s for s in S])
    fout.write('Case #'+str(t+1)+': ' + str(minNum)+'\n')

fin.close()
fout.close()
