def solve(n):
    if n==0:
        return "INSOMNIA"
    result = set()
    N = 0
    while len(result)<10:
        N += n
        result = result.union(set(list(str(N))))
    return N

filename = "A-large.in"
f = open(filename,"r")
fout = open(filename.replace(".in", ".out"), "w")
N = int(f.readline())
for i in range(N):
    n = int(f.readline())
    res = solve(n)
    print("Case #{}:".format(i+1), res)
    print("Case #{}:".format(i+1), res,file=fout)
f.close()
fout.close()
