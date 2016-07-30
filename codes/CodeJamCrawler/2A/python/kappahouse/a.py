# Rather Perplexing Showdown

conv = {'P': 'PR', 'R': 'RS', 'S': 'PS'}

def doit(c, n):
    if n == 0:
        return c
    return "".join(sorted([doit(x, n - 1) for x in conv[c]]))

def showdown(n, r, p, s):
    ret = sorted([doit(w, n) for w in ["P", "R", "S"]])
    for line in ret:
        if line.count('P') == p and line.count('R') == r and line.count('S') == s:
            return line
    return 'IMPOSSIBLE'

cases = int(raw_input())
for case in range(1, cases + 1):
    n, r, p, s = map(int, raw_input().split(' '))
    print "Case #" + str(case) + ": " + showdown(n, r, p, s)
