from multiprocessing import Pool


def solve(line):
    line = line.strip()
    res = 0
    for i in xrange(len(line)-1):
        if line[i]!= line[i+1]:
            res += 1
    if line[-1] == '-':
        res += 1
    print line, res
    return res


p = Pool(8)
with open("in.txt", "r") as fin:
    results = p.map(solve, fin.readlines()[1:])
    with open("out.txt", "w") as fout:
        i = 0
        for res in results:
            i += 1
            fout.write("Case #%d: %s\n" % (i, str(res)))
