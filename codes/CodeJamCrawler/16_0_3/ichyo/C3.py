import random
N = 32
J = 500
print("Case #1:")

def random_str():
    res = [random.randint(0, 1) for i in range(N)]
    res[0] = res[N-1] = 1
    return res

def parse(s, b):
    res = 0
    p = 1
    for i, c in enumerate(reversed(s)):
        res += c * p
        p *= b
    return res

def check(x):
    if x % 2 == 0: return 2
    i = 3
    MAX = 10
    while i * i <= x and i < MAX:
        if x % i == 0: return i
        i += 2
    return -1

st = {}
    
cnt = 0
while cnt < J:
    s = random_str()
    s_str = ''.join(str(x) for x in s)
    if s_str in st: continue
    st[s_str] = True
    ans = [check(parse(s, b)) for b in range(2, 11)]
    if ans.count(-1) == 0:
        print(s_str + ' ' + ' '.join(str(x) for x in ans))
        cnt += 1

