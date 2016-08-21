def input(file):
    F = open(file, "r")
    T = int(F.readline())
    for i in range(T):
        yield (i + 1), [int(e) for e in F.readline().split(" ")]

def solve(K, C, S):
    if 1 == C:
        if S >= K:
            r = [(1 + k) for k in range(K)]
        else:
            return "IMPOSSIBLE"
    else:
        if 2*S >= K:
            size = K**(C - 1)
            r = [size*subtree + (K - subtree) for subtree in range(K)]
        else:
            return "IMPOSSIBLE"

    return " ".join([str(e) for e in r])

out = open("D.out", "w")

#for (case, n) in input("Dsample.in"):
for (case, n) in input("D-small-attempt1.in"):
#for (case, n) in input("D-large.in"):
    print("Case #%d: %s" % (case, solve(n[0], n[1], n[2])), file = out)
