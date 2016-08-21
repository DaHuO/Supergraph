def cut(s):
    a = s[0]
    for i in s[1:]:
        if i != a[-1]:
            a = a + i
    if a[-1] == '+':
        return a[:-1]
    return a

def solve(x):
    x = cut(x)
    return len(x)

def tostk(n,p):
    s = bin(n)[2:]
    s = '0'*(p-len(s))+s
    a = ''
    for i in s:
        if i == '0':
            a = a + '+'
        else:
            a = a + '-'
    return a

# for i in range(1,11):
#     l = []
#     for j in range(2**i):
#         s = tostk(j,i)
#         print(s)
#         l.append(solve(s))
#         print(l[-1])
#     c = input()
#     #print(*l)

t = int(input())
for i in range(t):
    inp = input()
    print("Case #%d: %d"%(i+1, solve(inp)))
