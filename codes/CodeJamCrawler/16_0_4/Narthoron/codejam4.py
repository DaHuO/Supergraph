import math

x = input()
for i in range(int(x)):
    inputs = input().split()
    K = int(inputs[0])
    C = int(inputs[1])
    S = int(inputs[2])

    if S < math.ceil(K/2):
        print("Case #",i+1,": IMPOSSIBLE", sep='')
    elif K > 1 and S == 1:
        print("Case #",i+1,": IMPOSSIBLE", sep='')
    elif K == 1:
        print("Case #",i+1,": 1", sep='')
    elif C == 1:
        print("Case #",i+1,":", end='', sep='')
        for j in range(1,K+1):
            print(" ", j, end='', sep='')
        print()
    elif K == 2:
        print("Case #",i+1,": 2", sep='')
    else:
        print("Case #",i+1,": 2", end='', sep='')
        lastpos = 2
        max = K**2
        steam = K%2 == 0
        for j in range(S):
            lastpos += K - (lastpos%(K+1)) + K + 4
            if(lastpos <= max):
                print(" ", lastpos, end='', sep='')
            else:
                if not steam:
                    print(" ", max,end='', sep='')
                print()
                break
