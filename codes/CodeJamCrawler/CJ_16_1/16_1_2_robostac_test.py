import itertools
import math

def flatten(l):
    return itertools.chain.from_iterable(l)

def test(x,n,v,pos):
    if (v >= len(x)):
        t = list(map(list,zip(*x)))
        for i in n:
            if i not in t:
                raise  NameError("fail")
        return x
    for i in n:
        if x[v][pos] == i[pos]:
            try:
                t = x[:]
                t[v] = i
                nn = n[:]
                nn.remove(i)
                return test(t,nn,v+1,pos)
            except NameError:
                continue
    raise NameError("fail")



def solve(N,V):
    x = []
    res = N[:]
    for i in range(0,V):
        t = []
        for j in range(0,V):
            t.append("x")
        x.append(t)
    pos = 0

    c = 0
    v = (min(flatten(N)))
    for i in N:
        if i[0] == v:
            c += 1
    t = []
    for i in N:
        if i[0] == v:
            xx = x[:]
            xx[0] = i
            xx = list(map(list,zip(*xx)))
            nn = N[:]
            nn.remove(i)
            try:
                t = test(xx, nn, 0, pos)
                break
            except NameError:
                if (c == 1):
                    for j in nn:
                        for h in range(1,len(j)):
                            if i[h] == j[0]:
                                cc = xx[:]
                                cc[h] = j
                                cc = list(map(list, zip(*cc)))
                                bb = N[:]
                                bb.remove(i)
                                try:

                                    t = test(cc, bb, 1, h)
                                    break
                                except NameError:
                                    continue
                continue

    z = []
    for x in t:
        z.append(x)
    t = map(list,zip(*t))
    for x in t:
        z.append(x)
    for x in res:
        z.remove((x))
    return " ".join(map(str,z[0]))


def output_res(caseno,output, f):
    s = "Case #{}: {}".format(caseno,output)
    print(s)
    f.write(s + "\n")


f = open("input.txt")
f = open("B-small-attempt1.in")
outfile = open("output","w+")
T = int(f.readline())
for case in range(1, T + 1):
    N = [int(x) for x in f.readline().split()]
    V = []

    for i in range(0,2 * N[0] - 1):
        V.append([int(x) for x in f.readline().split()])
    output_res(case, solve(V,N[0]),outfile)

