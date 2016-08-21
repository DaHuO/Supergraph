def toi(x, base):
    ret = 0
    i = 0
    while (x >> i) > 0:
        ret += ((x >> i) & 1) * (base**i)
        i += 1
    return ret

def getd(x):
    if (x % 3 == 0):
        return 3
    m = 5
    f = False
    while x % m != 0 and m < min(x, 1000):
        f = not f
        if f:
            m += 2
        else:
            m += 4
    if m >= min(x, 1000):
        m = -1
    return m

t = int(input())
n,j = map(int, input().split())

ans = []
dss = []
x = 1 + (1 << (n-1))
for c in range(1, (1 << (n-2)) - 1):
    ds = []
    nx = x + (c << 1)
    for b in range(2, 11):
        d = getd(toi(nx, b))
        if d < 0:
            break
        ds.append(d)
    if len(ds) < 9:
        continue
    ans.append(nx)
    dss.append(ds)
    if len(ans) >= j:
        break

print('Case #1:')
for i in range(j):
    s = ''
    for k in range(n):
        s += str((ans[i] >> k) & 1)
    s = ''.join(reversed(s))
    for k in range(9):
        s += ' ' + str(dss[i][k])
    print(s)