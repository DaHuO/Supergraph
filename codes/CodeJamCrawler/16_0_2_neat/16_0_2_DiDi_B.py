T = int(input())


def f(s):
    s = s + "+"
    n = len(s)
    r = 0
    for t in range(n-1):
        if s[t] != s[t+1]:
            r = r + 1
    return r


for K in range(T):
    s = input()
    r = f(s)
    print("Case #" + str(K+1)+ ": " + str(r))
