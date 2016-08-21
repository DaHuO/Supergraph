import sys

lines = open(sys.argv[1]).readlines()

T = int(lines[0])

casenum = 0

for line in lines[1:]:
    casenum += 1
    vals = line.split()
    K = int(vals[0])
    C = int(vals[1])
    S = int(vals[2])

    if (K > C*S):
        print 'case #' + str(casenum) + ": IMPOSSIBLE"
        continue

    S = (K+C-1)/C


    # calculate value of C 1's base K
    # and also value of 'steps', = 0*K^{C-1} + 1*K^{C-2} ... + C-1
    ones = 0
    steps = 0
    laststeps = 0
    for i in range(C):
        ones = 1 + ones * K
        steps = i + steps * K
        if (C*S-K == C-i-1):
            laststeps = steps

    tiles = []
    for i in range(S-1):
        tiles.append(str(i*C*ones+steps+1))

    tiles.append(str((S-1)*C*ones+laststeps+1))

    print 'case #' + str(casenum) + ": " + ' '.join(tiles)
    
