
f = open("A-large.in", "r")
o = open("A-large.out", "w")

T = int(f.readline().strip())

for i in range(1, T+1):
    N = int(f.readline().strip())
    o.write("case #{}: ".format(i))
    if N == 0:
        o.write("INSOMNIA\n")
        continue
    L = set()
    k = 0
    while len(L) != 10:
        k += 1
        for j in str(N * k):
            L.add(j)
    o.write("{}\n".format(N*k))

f.close()
o.close()