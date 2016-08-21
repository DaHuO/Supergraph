def f(N,R,P,S):
    # Can't doitif more than half are anything
    if (N == 1):
        return ("P" * P) + ("R" * R) + ("S" * S)
    if 2 * max(R,P,S) > N:
        return "IMPOSSIBLE"
    a = (R + S - P) / 2
    b = (R + P - S) / 2
    c = (P + S - R) / 2
    # R = a + b
    # S = a + c
    # P = b + c
    sub = f(N/2,a,b,c)
    if sub == "IMPOSSIBLE":
        return sub
    return [t for z in sub for t in [z, "S" if z == "R" else "P" if z == "S" else "R"]]

def g(N,R,P,S):
    N = 2 ** N
    ans = f(N,R,P,S)
    if ans == "IMPOSSIBLE":
        return ans
    i = 1
    while i <= N:
        k = 0
        while k < N:
            if ans[k:k+i] > ans[k+i:k+2*i]:
                ans = ans[:k] + ans[k+i:k+2*i] + ans[k:k+i] + ans[k+2*i:]
            k += 2 * i
        i += i
    return "".join(ans)

from sys import stdin

for i in xrange(1,1+int(stdin.readline())):
    [N,R,P,S] = [int(z) for z in stdin.readline().split()]
    print "Case #{}: {}".format(i, g(N,R,P,S))
