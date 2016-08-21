import sys
import math

s = sys.stdin
t = int(s.readline())

for i in range(t):
    line = s.readline().split()
    K = int(line[0])
    C = int(line[1])
    S = int(line[2])
    numTiles = K**C

    if (C == 1):
        print('Case #' + str(i + 1) + ': ' + ' '.join(str(x + 1) for x in range(K)))
        continue


    partitionSize = K**(C - 1)
    if (S >= K):
        testNums = [];
        for j in range(K):
            testNums.append(j * partitionSize + 1) 
        print('Case #' + str(i + 1) + ': ' + ' '.join(str(x) for x in testNums))

    elif (S >= math.ceil(K / 2)):
        testNums = [];
        for j in range(math.ceil(K / 2)):
            testNums.append(j * 2 * partitionSize + j * 2 + 2)
        print('Case #' + str(i + 1) + ': ' + ' '.join(str(x) for x in testNums))
        
    else:
        print('Case #' + str(i + 1) + ': IMPOSSIBLE')
        

        




