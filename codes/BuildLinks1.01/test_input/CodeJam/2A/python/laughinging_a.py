def c(a,b):
    if a<b:
        return a+b
    return b+a

def h(n):
    R = ["R"]
    P = ["P"]
    S = ["S"]
    for i in xrange(1, n):
        R.append(c(R[i-1], S[i-1]))
        P.append(c(P[i-1], R[i-1]))
        S.append(c(S[i-1], P[i-1]))
    return R[-1],P[-1],S[-1]
        
def fit(n1,n2,n3,s):
    return [s.count("R"), s.count("P"), s.count("S")] == [n1, n2, n3]



f = open("A-large.in", "r")
t = int(f.readline().strip())
for i in xrange(t):
    s = f.readline().split()
    n, nR, nP, nS = [int(k) for k in s]    
    
    R, P, S = h(n+1)
    
    u = "z"
    for j in [R, P, S]:
        if fit(nR, nP, nS, j) and j<u:
            u = j

    if u=="z":
        u = "IMPOSSIBLE"
    print "Case #" + str(i+1) + ": " + str(u)










   
    

    
