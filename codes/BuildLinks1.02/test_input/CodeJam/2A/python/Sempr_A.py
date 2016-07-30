import sys
from collections import Counter

p={'S':"PS", 'R':"RS", 'P':"PR"}

def dfs(t, c):
    if t==0: 
        return c 
    new = p[c]
    l = dfs(t-1, new[0])
    r = dfs(t-1, new[1])
    if l < r:
        return l+r
    else:
        return r+l

def solve(t,N,R,P,S):
    a = dfs(N,'R')
    b = dfs(N,'P')
    c = dfs(N,'S')
    
    for x in sorted([a,b,c]):
        ct = Counter(list(x))
        if ct["S"] == S and ct["P"] == P and ct["R"] == R:
            print "Case #{}: {}".format(t+1, x)
            break
    else:
        print "Case #{}: IMPOSSIBLE".format(t+1 )



def main():
    T = int(sys.stdin.readline())
    for t in xrange(T):
        N,R,P,S = tuple([int(x) for x in sys.stdin.readline().strip().split()][:4])
        solve(t,N,R,P,S)
        
if __name__ == "__main__":
    main()

