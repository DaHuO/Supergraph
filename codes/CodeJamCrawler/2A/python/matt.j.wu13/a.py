t = int(input())


def solve(n, r, p, s):
    def get_strings(n, r, p, s, prevR, prevP, prevS):
        prevR.sort()
        prevP.sort()
        prevS.sort()
        
        if n == 0:
            if r == 1:
                return prevR[0]
            elif p == 1:
                return prevP[0]
            elif s == 1:
                return prevS[0]
        num = 2**(n - 1)
        if r > num or p > num or s > num:
            return "IMPOSSIBLE"

        rp_matches = (r + p - s) // 2
        rs_matches = r - rp_matches
        ps_matches = p - rp_matches

        r2 = rs_matches
        p2 = rp_matches
        s2 = ps_matches

        nextR = []
        nextP = []
        nextS = []

        for i in range(p2):
            a = prevP.pop(0)
            b = prevR.pop(0)
            nextP.append(min(a, b) + max(a, b))
        for i in range(r2):
            a = prevS.pop(0)
            b = prevR.pop(0)
            nextR.append(min(a, b) + max(a, b))
        for i in range(s2):
            a = prevP.pop(0)
            b = prevS.pop(0)
            nextS.append(min(a, b) + max(a, b))

        return get_strings(n - 1, r2, p2, s2, nextR, nextP, nextS)

    prevR = []
    prevP = []
    prevS = []
    for i in range(r):
        prevR.append("R")
    for i in range(p):
        prevP.append("P")
    for i in range(s):
        prevS.append("S")
    
    return get_strings(n, r, p, s, prevR, prevP, prevS)
        


for i in range(1, t + 1):
    line = input()
    n, r, p, s = line.split(" ")

    solution = solve(int(n), int(r), int(p), int(s))
    
    print("Case #{}: {}".format(i, solution))
