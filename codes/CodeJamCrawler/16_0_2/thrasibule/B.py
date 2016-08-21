import sys

def flip(what):
    return '-' if what=='+' else '+'

def solve(l, what):
    if len(l)==1:
        return 0 if l[0]==what else 1
    else:
        if l[-1]==what:
            return solve(l[:-1], what)
        else:
            return 1 + solve(l[:-1], flip(what))

fh = open(sys.argv[1])
N = int(next(fh))
for i in range(N):
    line = next(fh).rstrip()
    print("Case #{0}: {1}".format(i+1, solve(line, '+')))
fh.close()
