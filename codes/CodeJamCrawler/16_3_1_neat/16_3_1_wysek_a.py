def solve():
    N = int(input())
    P = [int(x) for x in input().split()]
    left = sum(P)
    res = []
    while left > 0:
        maxP = 0
        maxP2 = -1
        i = 1
        while i < len(P):
            if P[i] > P[maxP]:
                maxP = i
                maxP2 = -1
            elif P[i] == P[maxP] and maxP2 == -1:
                maxP2 = i
            i += 1
            
        if left == 3:
            res.append(chr(65 + maxP))
            P[maxP] -= 1
            left -= 1
        elif maxP2 == -1:
            if P[maxP] >= 2:
                res.append(chr(65 + maxP) + chr(65 + maxP))
                P[maxP] -= 2
                left -= 2
            else:
                res.append(chr(65 + maxP))
                P[maxP] -= 1
                left -= 1
        else:
            res.append(chr(65 + maxP) + chr(65 + maxP2))
            P[maxP] -= 1
            P[maxP2] -= 1
            left -= 2
    
    return " ".join(res)

def main():
    T = int(input())
    for t in range(1, T+1):
        print("Case #%d: %s" % (t, solve()))

if __name__ == "__main__":
    main()
