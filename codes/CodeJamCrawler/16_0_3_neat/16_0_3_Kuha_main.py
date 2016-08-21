def prime (k):
    it = 2
    while it * it <= k:
        if k % it == 0: return it
        if it == 100000: return 0
        it += 1
    return 0

def tobase (v, k):
    s = 0
    m = 1
    for im in range(0, len(v)):
        s += m * (v[len(v) - im - 1])
        m *= k
    return s

out = open("large.out", "w")
out.write("Case #1:\n")
n = 32
j = 500
foo = 0
i = 0
while foo != j:
    ti = (1<<(n - 1)) | (i<<1) | 1
    v = []
    q = []
    for x in range(0, n):
        v.append(ti % 2)
        ti //= 2
    v = list(reversed(v))
    for ix in range(2, 11):
        lol = prime(tobase(v, ix))
        if lol != 0:
            q.append(lol)
        else:
            break
    #print(str(i) + " => " + str(len(q)))
    if len(q) == 9:
        foo += 1
        for x in v:
            out.write(str(x))
        out.write(" ")
        for x in q:
            out.write(str(x) + " ")
        out.write("\n")
        print(str(i) + " -> " + str(foo) + "/" + str(j))
    i += 1
out.close();
