import sys
ts = int(raw_input())

ns = [ "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" ]

def let_count(s):
    r = {}
    for l in s:
        if l in r: r[l] += 1
        else: r[l] = 1
    return r

def sub_let(lc, d):
    for c in ns[d]:
        if lc[c] > 1: lc[c] -= 1
        else: del lc[c]
    return lc, d

def find_num(lc):
    if 'Z' in lc: return sub_let(lc,0)
    if 'W' in lc: return sub_let(lc,2)
    if 'U' in lc: return sub_let(lc,4)
    if 'X' in lc: return sub_let(lc,6)
    if 'G' in lc: return sub_let(lc,8)
    if 'R' in lc: return sub_let(lc,3)
    if 'O' in lc: return sub_let(lc,1)
    if 'F' in lc: return sub_let(lc,5)
    if 'V' in lc: return sub_let(lc,7)
    return sub_let(lc,9)


for t in range(ts):
    print "Case #{}:".format(t+1),

    s = raw_input()

    lc = let_count(s)
    sol = []
    while len(lc.keys()) > 0:
        lc, d = find_num(lc)
        sol += [d]
    print "".join([str(x) for x in sorted(sol)])
