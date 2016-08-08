import sys
import itertools

cases = int(sys.stdin.readline().strip())

def find_solution(r, s, p):
    #print (r,s,p)
    if r < 0:
        return None
    if s < 0:
        return None
    if p < 0:
        return None
    if r + s + p == 1:
        if r:
            return ["R"]
        if s:
            return ["S"]
        if p:
            return ["P"]
        assert False
    for x in range(r+1):
        y = s-x
        z = r-x
        if y+z != p:
            continue
        #print "xxx", x, y, z, x+z, x+y, y+z
        res = find_solution(x,y,z)
        if res:
            return best(back(res))
    return None

def expand(data):
    x = ["RS", "SR"]
    y = ["PS", "SP"]
    z = ["PR", "RP"]
    res = data.replace("R", "X")
    res = res.replace("S", "Y")
    res = res.replace("P", "Z")
    for xx in x:
        tmpx = res.replace("X", xx)
        for yy in y:
            tmpy = tmpx.replace("Y", yy)
            for zz in z:
                tmpz = tmpy.replace("Z", zz)
                yield tmpz

def best(data):
    data = list(data)
    res = []
    for order in itertools.permutations(["P","R","S"]):
        #print data
        res.append(max(data, key=lambda string:[order.index(s) for s in string]))
    return res

def back(data):
    for res in data:
        for x in expand(res):
            yield x


def solve(case):
    n, r, p, s = map(int, sys.stdin.readline().strip().split())
    assert r+p+s == 2**n
    res = find_solution(r, s, p)
    if not res:
        res = "IMPOSSIBLE"
    else:
        res = res[-1]
    print "Case #%d: %s" % (case, res)

for i in range(cases):
    solve(i+1)
