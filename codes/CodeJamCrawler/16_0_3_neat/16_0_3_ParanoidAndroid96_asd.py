import random

def isprime(n):
    if n == 2:
        return True, 2
    if n == 3:
        return True, 3
    if n % 2 == 0:
        return False, 2
    if n % 3 == 0:
        return False, 3
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False, i
        i += w
        w = 6 - w
    return True, 0

def check(s):
    global pw
    global ans
    global n
    if s[:1:-1] in ans:
        return 0, []
    factors = []
    for base in range(2, 11):
        ffs = 0
        for i in range(0, len(s)):
            ffs += pw[base][i] * (ord(s[i]) - ord('0'))
        ok, f = isprime(ffs)
        if ok == True:
            return 0, []
        factors.append(f)
    return 1, factors
        

n, J = map(int, input().split())
pw = []
pw.append(0)
pw.append(1)
ans = []
divs = []
for i in range(2, 11):
    cur = [1 for i in range(33)]
    cur.append(1)
    for j in range(1, 33):
        cur[j] = cur[j - 1] * i
    pw.append(cur)
m = 2 ** (n - 3)
p = 2 ** (n - 1)
while len(ans) < J:
    num = random.randint(0, m)
    num = p + num * 2 + 1
    a, b = check(str(bin(num))[2:])
    if a == 1 and bin(num)[:1:-1] not in ans:
        ans.append(bin(num)[:1:-1])
        divs.append(b)
for i in range(len(ans)):
    print(ans[i], end = ' ')
    for j in divs[i]:
        print(j, end = ' ')
    print()
    
