import sys
import math
sys.setrecursionlimit(10000)

T = int(raw_input())

for _test in range(1, T + 1):
    answer = 0

    N = int(raw_input())

    data = []

    for _ in range(N):
        data.append(raw_input().split())

    mask = 1
    #print N
    while mask < (1 << N):
        #print "mask", mask,
        valid = []  # not faked

        local_ans = 0

        x = mask

        for i in range(N*2):
            if x == 0:
                break

            if x & 1 == 1:
                valid.append(i)

            x >>= 1

        #print valid,

        for i in range(N):
            used = False
            if i not in valid:
                #print "check", i, "llevo", local_ans
                for q in range(len(valid)):
                    a = valid[q]
                    for p in range(q +1, len(valid)):
                        b = valid[p]
                        if data[a][0] == data[i][0] and data[b][1] == data[i][1]:
                            used = True
                        elif data[a][1] == data[i][1] and data[b][0] == data[i][0]:
                            used = True

            if used:
                local_ans += 1

        answer = max(local_ans, answer)

        mask += 1
        #break
    print "Case #{}: {}".format(_test, answer)

"""
3
3
HYDROCARBON COMBUSTION
QUAIL BEHAVIOR
QUAIL COMBUSTION
3
CODE JAM
SPACE JAM
PEARL JAM
2
INTERGALACTIC PLANETARY
PLANETARY INTERGALACTIC

Case #1: 1
Case #2: 0
Case #3: 0
"""
