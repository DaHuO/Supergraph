def countingSheep(n):
    counts = {str(i):0 for i in range(0,10)}
    ns = [n]
    while (0 in counts.values()):
        if (n * 10) in ns:
            return None
        ns.append(n)
        for digit in str(n):
            counts[digit] += 1
        n += ns[0]
    return ns[-1]


with open("A-large.in", "r") as f:
    nCases = int(f.readline())
    with open("A-large.out", "w") as fout:
        for iCase in range(nCases):
            n = int(f.readline())
            print("Case #%d: %s" % (iCase+1, countingSheep(n) or "INSOMNIA"), file=fout)

# print(countingSheep(1692))
# print(countingSheep(1))
# print(countingSheep(2))
# print(countingSheep(11))
# print(countingSheep(0) or "INSOMNIA")
# print("%s" % (3))
