def input(file):
    F = open(file, "r")
    T = int(F.readline())
    for i in range(T):
        yield (i + 1), F.readline().strip()

def solve(S):
    def stepFromLeft(s):
        start = s.find("-")
        if -1 == start: return s

        end = s.find("+", start)
        if -1 == end: end = len(s)
        else: end = end

        return "".join(['+' if s[i] == '-' else '-' for i in range(end)]) + s[end: len(s)]

    def count(s):
        return sum(1 if s[i] != s[i + 1] else 0 for i in range(len(s) - 1))

    q = [(S, 0)]
    while 0 != len(q):
        node, pathLen = q.pop(0)
        if '-' not in node: return pathLen

        nodeNext = stepFromLeft(node)
        cNode, cNodeNext = count(node), count(nodeNext)
        if cNode > cNodeNext or (cNode == cNodeNext and node < nodeNext): q.append((nodeNext, pathLen + 1))
        elif '-' not in nodeNext: return pathLen + 1

    return -1

out = open("B.out", "w")

#for (case, S) in input("Bsample.in"):
#for (case, S) in input("B-small-attempt0.in"):
for (case, S) in input("B-large.in"):
    print("Case #%d: %s" % (case, solve(S)), file = out)
    #print("Case #%d: %s" % (case, solve(S)))
