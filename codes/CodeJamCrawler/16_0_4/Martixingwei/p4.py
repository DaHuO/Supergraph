def solve(K,C,S):
    if K<=S:
        return [str(i+1) for i in range(0, K**C, K**(C-1))]
    return ["NOT IMPLEMENTED"]

filename = "D-small-attempt0.in"
f = open(filename,"r")
fout = open(filename.replace(".in", ".out"), "w")
N = int(f.readline())
for i in range(N):
    K,C,S = [int(j) for j in f.readline().split()]
    res = ' '.join(solve(K,C,S))
    print("Case #{}:".format(i+1), res)
    print("Case #{}:".format(i+1), res,file=fout)
f.close()
fout.close()
