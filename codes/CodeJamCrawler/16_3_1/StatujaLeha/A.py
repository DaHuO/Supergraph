def input(file):
    F = open(file, "r")
    T = int(F.readline())
    for i in range(T):
        F.readline()
        yield (i + 1), [int(e) for e in F.readline().strip().split(' ')]

def solve(S):
    def first(v, seq):
        for i in range(len(seq)):
            if seq[i] == v: return i

        return -1

    def last(v, seq):
        for i in range(len(seq)):
            if seq[len(seq) - 1 - i] == v: return len(seq) - 1 - i

        return -1

    before = [0] * len(S)
    plan = []
    T = sum(S)
    current = 0
    while current != T:
        beforeS = list(sorted([(before[b] if S[b] > before[b] else 10**9, b) for b in range(len(before))], key= lambda x: x[0]))
        #l = first(beforeS[0], before)
        #r = last(beforeS[1], before)
        l, r = beforeS[0][1], beforeS[1][1]
        #print(before, beforeS, l, r)

        #if -1 == l and -1 == r:
        #if -1 == l and -1 == r:
        #    break

        if beforeS[1][0] == 10**9:
            current += 1
            before[l] += 1
            plan.append([l])
        else:
            current += 2
            before[l] += 1
            before[r] += 1
            plan.append([l, r])


    #print(plan, S, before)

    return " ".join(["".join([chr(c + ord('A')) for c in e]) for e in plan[::-1]])

out = open("A.out", "w")

#for (case, S) in input("Asample.in"):
#for (case, S) in input("A-small-attempt0.in"):
for (case, S) in input("A-large.in"):
#for (case, S) in input("A-small-practice.in"):
#for (case, S) in input("A-large-practice.in"):
    print("Case #%d: %s" % (case, solve(S)), file = out)
