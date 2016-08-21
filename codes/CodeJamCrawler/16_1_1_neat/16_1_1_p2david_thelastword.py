size =  "large"


def solve(S):

    sol =S[0]
    for i in range(1, len(S)):
        if S[i]<sol[0]:
            sol = sol + S[i]
        else:
            sol = S[i]+sol
    print(sol)
    return sol



f = open('A-%s.in' % size)
o = open('A-%s.out' % size, 'w')
n = int(f.readline())
for i in range(1, n+1):
    S = f.readline().rstrip()
    sol = solve(S)
    o.write("Case #%d: %s\n" % (i, sol))
f.close()
o.close()
