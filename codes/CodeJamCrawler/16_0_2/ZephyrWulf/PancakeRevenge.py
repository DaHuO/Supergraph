def minFlips(inp, bottomReq):
    if len(inp) == 0:
        return 0
    if inp[-1] == bottomReq:
        return minFlips(inp[:-1], bottomReq)
    else:
        nextBottom = "-" if bottomReq == "+" else "+"
        return minFlips(inp[:-1], nextBottom) + 1

file = "large"
fin = open(file + ".in", 'r')
fout = open(file + ".out", 'w')

cases = int(fin.readline())

for i in range(cases):
    inp = fin.readline().strip()
    result = minFlips(inp, "+")
    fout.write("Case #" + str(i+1) + ": " + str(result) + "\n")