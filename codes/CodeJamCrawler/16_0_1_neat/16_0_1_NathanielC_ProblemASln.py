def solve(n):
    if n == 0:
        return "INSOMNIA"

    m = n
    obs = set(str(m))
    while len(obs) < 10:
        m += n
        obs = obs.union(str(m))
    return m

fin = open("A-large.in", "r")
fout = open("A-large.out", "w")

for t in xrange(1, int(fin.readline()) + 1):
    sln = solve(int(fin.readline()))
    fout.write("Case #" + str(t) + ": " + str(sln) + "\n")

fout.close()
