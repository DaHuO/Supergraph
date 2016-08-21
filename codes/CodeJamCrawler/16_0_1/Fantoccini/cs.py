from multiprocessing import Pool


def solve(line):
    n = int(line.strip())
    if n == 0:
        return "INSOMNIA"
    s = set()
    res = 0
    while len(s) < 10:
        res += n
        tres = res
        while tres > 0:
            s.add(tres % 10)
            tres /= 10
    print n, res
    return res


p = Pool(8)
with open("in.txt", "r") as fin:
    results = p.map(solve, fin.readlines()[1:])
    with open("out.txt", "w") as fout:
        i = 0
        for res in results:
            i += 1
            fout.write("Case #%d: %s\n" % (i, str(res)))
