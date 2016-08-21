import sys

def solve(st):
    # print(st)
    chars = list(st)
    poss = [[chars[0]]]
    for char in chars[1:]:
        newpos = []
        for p in poss:
            newpos.append([char]+p)
            newpos.append(p+[char])
        poss = newpos

    return ''.join(sorted(poss)[-1])

def solve(st):
    # print(st)
    chars = list(st)
    best = chars[0]
    for char in chars[1:]:
        one = char+best
        two = best+char
        best = max(one,two)

    return ''.join(best)

with open(sys.argv[1]) as f:
    t = int(f.readline())
    for i in range(t):
        # n = int(f.readline())
        # ps = [el for el in f.readline()[:-1].split()]
        st = f.readline()[:-1]
        sol = solve(st)
        print('Case #%d: %s' % (i+1,sol))
