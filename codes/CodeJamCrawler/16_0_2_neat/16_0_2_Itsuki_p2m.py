import sys

def reverse(P):
    for i in range(0, len(P)):
        if P[i] == '+':
            P = P[:i] + '-' + P[i+1:]
        else:
            P = P[:i] + '+' + P[i+1:]
    return P

def flipCake(i, P):
    tP = P[0:i+1]
    tP = reverse(tP[::-1])
    tP = tP + P[i+1:]
    return tP

def solve(P):
    result = 0
    cakes = {}
    init = '+'*len(P)
    cakes[init] = 0

    if init == P:
        return 0

    while True :
        keys = [t for t in cakes.keys() if cakes[t] == result]
        result = result + 1
        for k in keys: 
            for i in range(0, len(k)):
                new = flipCake(i, k)
                if new == P:
                    return result
                if (new in cakes.keys()) == False:
                    cakes[new] = result
    return result
    
def main():
    result = []
    T = sys.stdin.readline().strip()
    for i in range(0, int(T)):
        P = sys.stdin.readline().strip().split()
        result.append(solve(str(P[0])))

    for i in range(0, len(result)):
        print("Case #%d:" % (i+1)), result[i]

if __name__=="__main__":
    main()