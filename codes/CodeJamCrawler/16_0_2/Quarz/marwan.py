f = open("D:/B-large.in", "r")
w = open("D:/B-large.out", "w")

t = int(f.readline())
i = 1

for p in f.read().split('\n'):
    if len(p) == 0:
        break
    s = 0
    while p.count('+') != len(p):
        b = 0
        while b+1 < len(p) and p[b+1] == p[b]:
            b += 1

        p = (p[:b+1]).replace('+', '*').replace('-', '+').replace('*', '-')[::-1] + p[b+1:]
        s += 1

    w.write("Case #" + str(i) + ": " + str(s) + "\n")
    i += 1

f.close()
w.close()