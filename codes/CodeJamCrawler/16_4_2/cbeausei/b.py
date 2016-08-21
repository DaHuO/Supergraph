import sys
sys.setrecursionlimit(1000000000)

INF = 1000000000
val = 0.0

def pp(s):
    s = str(s)
    sys.stderr.write(s + '\n')
    sys.stderr.flush()
    
def add():
    # pp(tab2)
    global val
    j = 0
    prob = 1.0
    for i in range(n):
        if tab[i] == 1:
            if tab2[j] == 1:
                prob *= p[i]
            else:
                prob *= (1.0 - p[i])
            j += 1
    val += prob

def find2(r, n):
    if n == 0:
        add()
    else:
        if r > 0:
            tab2[n - 1] = 1
            find2(r - 1, n - 1)
        if r < n:
            tab2[n - 1] = 0
            find2(r, n - 1)

def test():
    global opti, val
    # pp(tab)
    val = 0.0
    find2(k // 2, k)
    opti = max(opti, val)

def find(r, n):
    if n == 0:
        test()
    else:
        if r > 0:
            tab[n - 1] = 1
            find(r - 1, n - 1)
        if r < n:
            tab[n - 1] = 0
            find(r, n - 1)

T = int(input())
for N in range(1, T + 1):
    out = 'Case #' + str(N) + ': '

    n, k = map(int, input().split())
    p = [float(i) for i in input().split()]
    tab = [0 for _ in range(n)]
    tab2 = [0 for _ in range(k)]
    
    opti = 0.0
    
    find(k, n)
    out +="%.07f" % opti

    out += '\n'
    sys.stdout.write(out)
    sys.stdout.flush()
    sys.stderr.write(out)
    sys.stderr.flush()