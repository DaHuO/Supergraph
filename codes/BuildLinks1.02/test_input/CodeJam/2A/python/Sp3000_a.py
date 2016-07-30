from functools import lru_cache

def valid(a,b,c):
    return max([abs(a-b),abs(b-c),abs(a-b)]) <= 1


@lru_cache(None)
def solve(P,R,S):
    if P+R+S == 1:
        if P:
            return 'P'
        if R:
            return 'R'
        if S:
            return 'S'
        
    a = b = c = (P+R+S)//6
    d = e = f = (P+R+S)//6

    X = P - a - d
    Y = R - b - e
    Z = S - c - f

    if (X,Y,Z) == (1,1,0):
        a += 1
        e += 1

    elif (X,Y,Z) == (1,0,1):
        a += 1
        f += 1

    elif (X,Y,Z) == (0,1,1):
        b += 1
        f += 1

    elif (X,Y,Z) == (2,0,0):
        a += 1
        d += 1

    elif (X,Y,Z) == (0,2,0):
        b += 1
        e += 1

    elif (X,Y,Z) == (0,0,2):
        c += 1
        f += 1

    elif (X,Y,Z) == (1,1,2):
        a += 1
        c += 1
        e += 1
        f += 1

    elif (X,Y,Z) == (1,2,1):
        a += 1
        b += 1
        e += 1
        f += 1

    elif (X,Y,Z) == (2,1,1):
        a += 1
        b += 1
        d += 1
        f += 1

    else:
        print(X,Y,Z)

    return solve(a,b,c) + solve(d,e,f)


with open("A-large.in") as infile:
    with open("a.out", "w") as outfile:
        cases = int(next(infile))

        for case in range(1, cases+1):     
            N, R, P, S = list(map(int, next(infile).split()))

            if not valid(P,R,S):
                print("Case #{}: IMPOSSIBLE".format(case), file=outfile)
                continue

            print("Case #{}: {}".format(case, solve(P,R,S)), file=outfile)

assert solve(6,5,5) == "PRPSPRRSPRPSPSRS"
assert solve(1,2,1) == "PRRS"
assert solve(1,1,2) == "PSRS"
