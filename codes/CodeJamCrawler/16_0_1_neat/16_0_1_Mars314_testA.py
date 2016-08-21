def solve(n):
    if n == 0:
        return 'INSOMNIA'
    times = 0
    a = {i:0 for i in range(10)}
    while not all(a.values()):
        times += 1
        for ch in str(n * times):
            a[int(ch)] = 1
    return times * n


T = input()
for t in range(T):
    print "Case #%s: %s " % (t + 1,solve(input()))
