def input(file):
    F = open(file, "r")
    T = int(F.readline())
    for i in range(T):
        yield (i + 1), [e for e in F.readline().strip().split(' ')]

def solve(S):
    def F(l):
        if 0 == len(l):
            yield ""
        else:
            if l[0] == '?':
                for e in range(10):
                    for w in F(l[1:]):
                        yield str(e) + w
            else:
                for w in F(l[1:]):
                    yield l[0] + w

    CS, JS = str(10**20), str(0)
    for cs in F(S[0]):
        for js in F(S[1]):
            c, j = int(cs), int(js)
            C, J = int(CS), int(JS)
            p, q = abs(c - j), abs(C - J)
            if p <= q:
                if p == q:
                    if c < C:
                        CS, JS = cs, js
                    elif j < J:
                        CS, JS = cs, js
                else:
                    CS, JS = cs, js

    return "%s %s" % (CS, JS)

out = open("B.out", "w")

#for (case, S) in input("Bsample.in"):
for (case, S) in input("B-small-attempt0.in"):
#for (case, S) in input("B-large.in"):
#for (case, S) in input("B-small-practice.in"):
#for (case, S) in input("B-large-practice.in"):
    print("Case #%d: %s" % (case, solve(S)), file = out)