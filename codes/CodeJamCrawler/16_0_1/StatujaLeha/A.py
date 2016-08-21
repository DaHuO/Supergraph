def input(file):
    F = open(file, "r")
    T = int(F.readline())
    for i in range(T):
        yield (i + 1), int(F.readline())

def solve(n):
    D = [False] * 10

    if 0 == n: return "INSOMNIA"

    i = 1
    while False in D:
        next = i*n

        for d in str(next):
            D[ord(d) - ord('0')] = True

        i += 1

    return str(next)

#print(solve(1))
#print(solve(2))
#print(solve(11))
#print(solve(1692))

out = open("A.out", "w")

#for (case, n) in input("Asample.in"):
#for (case, n) in input("A-small-attempt0.in"):
for (case, n) in input("A-large.in"):
    print("Case #%d: %s" % (case, solve(n)), file = out)
