import sys
import math

def solve(rem, h, k):
    if len(rem) == 0:
        return 0
    if h == 1:
        return rem[0]
    if len(rem) == 1:
        return rem[0] + k*(solve(rem,h-1, k)-1) 
    return rem[-1] + k*(solve(rem[:-1], h-1, k)-1)

with open(sys.argv[1]) as infile:
    with open(sys.argv[1]+".out", 'w') as outfile:
        nt = int(infile.readline())
        for t in range(1, nt+1):
            line = map(int,  infile.readline().split(" "))
            k = line[0]
            c = line[1]
            s = line[2]

            outfile.write("Case #" + str(t) + ": ")
            if k/c > s or (k % c != 0 and k/c+1 > s):
                outfile.write("IMPOSSIBLE")
            elif c >= k:
                outfile.write(str(solve(list(range(1,k+1)), c, k)))
            else:
                res = []
                i = 1
                while i+c <= k:
                    res.append(solve(list(range(i,i+c)), c, k))            
                    i += c
                if i <= k:
                    res.append(solve(list(range(i,k+1)), c, k))
                outfile.write(" ".join(map(str, res)))

            outfile.write("\n")
