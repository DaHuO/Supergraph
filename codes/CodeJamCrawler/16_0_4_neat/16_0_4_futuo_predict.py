from math import ceil

def solve(K, C, S):

    if( C == 1 ):
        positions = [i for i in range(1,K+1)]
        if( S < K ):
            return "IMPOSSIBLE"
        else:
            return " ".join(str(i) for i in positions)

    positions = []
    unknown = K
    count = 0
    while( unknown > 0 ):
        pos = K**(C-1) * (count+1) - count
        positions += [pos]

        if( pos - (count * K**(C-1)) == count + 1 ):
            unknown -= 1
        else:
            unknown -= 2
        count += 1

    if( len(positions) > S ):
        return "IMPOSSIBLE"
    else:
        return " ".join(str(i) for i in positions)

NTT = int(input())

for TC in range(1,NTT+1):
    K,C,S = [int(i) for i in input().split(" ")]
    print("Case #{0}: {1}".format(TC, solve(K,C,S)))

