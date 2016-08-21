def c(n):
    if n == 0:
        return "INSOMNIA"

    a = [0] * 10
    i = 0
    while True:
        i = i + 1
        z = n * i
        for ch in str(z):
            a[int(ch)] = 1
        if sum(a)==10:
            return str(z)


T = int(input())
for t in range(1,T+1):
    N = int(input())
    print("Case #%d: %s" % (t,c(N)))



