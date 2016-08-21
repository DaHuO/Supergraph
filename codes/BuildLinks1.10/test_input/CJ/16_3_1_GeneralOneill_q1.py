import string

def remove(l):
    alph = string.ascii_lowercase
    rtn = ''
    while sum(l) > 0:
        hi = max(l)
        rtn += alph[l.index(hi)]
        l[l.index(hi)] -= 1
        hi = max(l)
        if float(hi) / sum(l) > .5:
            rtn += alph[l.index(hi)]
            l[l.index(hi)] -= 1
        rtn += ' '
    return rtn

cases = int(raw_input())
for case in range(cases):
    n = int(raw_input())
    l = raw_input().strip().split()
    l = map(int, l)
    out = remove(l)
    print("Case #" + str(case+1) + ": " + out)
