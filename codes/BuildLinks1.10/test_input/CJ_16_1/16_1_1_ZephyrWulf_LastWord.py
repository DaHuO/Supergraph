def lastWord(word):
    a = []
    for c in word:
        if len(a) == 0:
            a = [c]
            continue
        if ord(c) >= ord(a[0]):
            a = [c] + a
        else:
            a.append(c)

    return "".join(a)

file = "large"
fin = open(file + ".in", 'r')
fout = open(file + ".out", 'w')

cases = int(fin.readline())

for i in range(cases):
    inp = fin.readline().strip()
    result = lastWord(inp)
    fout.write("Case #" + str(i+1) + ": " + str(result) + "\n")