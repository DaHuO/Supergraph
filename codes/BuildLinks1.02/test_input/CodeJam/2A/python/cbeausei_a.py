import sys
sys.setrecursionlimit(1000000000)

INF = 1000000000
def test(s):
    s2 = ""
    if len(s) == 1:
        return(True)
    else:
        for i in range(len(s) // 2):
            v = 'r'
            x = s[2 * i]
            y = s[2 * i + 1]
            if x == y:
                return(False)
            if x == 'P':
                if y == 'R':
                    v = 'P'
                else:
                    v = 'S'
            if x == 'S':
                if y == 'P':
                    v = 'S'
                else:
                    v = 'R'
            if x == 'R':
                if y == 'S':
                    v = 'R'
                else:
                    v = 'P'
            s2 += v
        return(test(s2))

def find(r, p, s, st):
    if r + p + s == 0:
        if test(st):
            return(st, True)
    if p > 0:
        news = st + "P"
        v, b = find(r, p - 1, s, news)
        if b:
            return(v, b)
    if r > 0:
        news = st + "R"
        v, b = find(r - 1, p, s, news)
        if b:
            return(v, b)
    if s > 0:
        news = st + "S"
        v, b = find(r, p, s - 1, news)
        if b:
            return(v, b)
    return("", False)
        
T = int(input())
for N in range(1, T + 1):
    out = 'Case #' + str(N) + ': '

    n, r, p, s = map(int, input().split())
    v, b = find(r, p, s, "")
    if b:
        out += v
    else:
        out += 'IMPOSSIBLE'

    out += '\n'
    sys.stdout.write(out)
    sys.stdout.flush()
    sys.stderr.write(out)
    sys.stderr.flush()