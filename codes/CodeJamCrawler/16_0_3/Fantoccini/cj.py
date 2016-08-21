from multiprocessing import Pool


def solve(line):
    line = line.strip().split()
    n = int(line[0])
    j = int(line[1])
    res = "\n"
    for i in xrange(1 << (n - 2)):
        cj = "1" + ("{0:b}".format(i)).zfill(n - 2) + "1"
        ps = 0
        tres = cj
        for base in xrange(2, 11):
            num = int(cj, base)
            cd = 2
            while cd < 10000:
                if num % cd == 0:
                    tres += " %d" % (cd,)
                    break
                cd += 1
            if num % cd == 0:
                ps += 1
            else:
                break
        if ps == 9:
            res += tres + "\n"
            print(tres)
            j -= 1
            if j == 0:
                break
            print j
    return res


p = Pool(8)
with open("in.txt", "r") as fin:
    results = p.map(solve, fin.readlines()[1:])
    with open("out.txt", "w") as fout:
        i = 0
        for res in results:
            i += 1
            fout.write("Case #%d: %s\n" % (i, str(res)))
