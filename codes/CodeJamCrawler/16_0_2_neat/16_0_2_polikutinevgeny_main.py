inf = open('input.txt', 'r')
ouf = open('output.txt', 'w')
t = int(inf.readline())
for i in range(t):
    s = []
    for j in inf.readline().strip():
        s.append(True if j == '+' else False)
    q = 0
    while len(s) > 0:
        t = len(s)
        while t > 0 and s[t - 1]:
            t -= 1
        if t <= 0:
            break
        s = s[:t]
        if s[0]:
            d = t
            while d > 0 and not s[d - 1]:
                d -= 1
            s = ([not k for k in s[:d]] + s[d:t])[::-1]
        else:
            s = [not k for k in s][::-1]
        q += 1
    ouf.write('Case #{}: {}\n'.format(i + 1, q))
inf.close()
ouf.close()