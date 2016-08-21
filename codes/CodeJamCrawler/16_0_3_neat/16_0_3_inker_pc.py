import itertools

def gen(n):
    assert n >= 2
    od = range(1, n, 2)
    ed = range(2, n, 2)
    [od, ed][n%2].pop()
    dd = 2 if n%2 else 0

    for nd in range(dd, min(len(od), len(ed)-dd)):
        for sod in itertools.combinations(od, nd):
            for sed in itertools.combinations(ed, nd):
                res = ["0"]*n
                for x in sod+sed+(0, n-1):
                    res[n-1-x] = "1"
                yield "".join(res)

for case in range(1, int(raw_input())+1):
    print "Case #%d:"%case
    n, j = map(int, raw_input().split())
    for i in gen(n):
        assert all(map(lambda c: int(i, c)%(c+1)==0, range(2, 11)))
        print i+" "+" ".join(map(str, range(3, 12)))
        j -= 1
        if j <= 0:
            break
    else:
        assert False, "Not Enough"
