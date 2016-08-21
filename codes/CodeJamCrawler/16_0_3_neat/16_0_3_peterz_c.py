import random
def gen(n):
    ret = 1
    for i in range(n - 2):
        ret += random.choice((0, 1)) * (2 ** (i + 1))
    ret += 2 ** (n - 1)
    return ret

def find(x):
    ret = []
    for base in range(2, 11):
        tmp = 0
        for i in range(n):
            tmp += (1 if (x & (2 ** i)) else 0) * base ** i
        ok = -1
        for i in range(2,1000):
            if tmp % i == 0:
                ok = i
                break
        if ok == -1:
            return []
        ret.append(ok)
    return ret

random.seed(123)
input()
print('Case #1:')
n, m = (int(_) for _ in input().split())
ans = {}
while len(ans) < m:
    tmp = gen(n)
    if tmp in ans:
        continue
    pf = find(tmp)
    if len(pf) == 9:
        ans[tmp] = pf
for ky in ans:
    tmp = 0
    for i in range(n):
        tmp += (1 if (ky & (2 ** i)) else 0) * 10 ** i
    lst = ans[ky]
    print(tmp, ' '.join([str(_) for _ in lst]))

