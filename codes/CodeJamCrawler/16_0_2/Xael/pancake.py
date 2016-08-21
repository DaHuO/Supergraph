def flip(array, imax):
    k = list(reversed(array[0:imax+1]))
    for i in range(len(k)):
        array[i] = not k[i]

def getMaxPosIndex(lineB):
    for i in range(len(lineB)):
        if lineB[i] == False:
            return i - 1
    return len(lineB) - 1

fi = open('B-large.in', 'r')
fo = open('outputB.txt', 'w')

T = int(fi.readline())

for t in range(T):

    line = fi.readline()
    N = len(line) - 1
    lineB = [False] * N
    for i in range(N):
        if line[i] == '+':
            lineB[i] = True
        elif line[i] == '-':
            lineB[i] = False
    steps = 0
    finished = False
    p = N - 1

    while finished == False:
        if lineB == [True] * N:
            finished = True
            break
        while lineB[p] == True:
            p -= 1
        if lineB[0] == False:
            flip(lineB, p)
            steps += 1
        else:
            flip(lineB, getMaxPosIndex(lineB))
            steps += 1
            flip(lineB, p)
            steps += 1

    
    print('Case {0}: {1}'.format(t+1, steps))
    fo.write('Case #{0}: {1}\n'.format(t+1, steps))
fi.close()
fo.close()
        
