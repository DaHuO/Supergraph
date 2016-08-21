T = int(input())

def solve(N):

    if N == 0:
        return "INSOMNIA"

    i = 1
    chiffres = ['{}'.format(k) for k in range(10)]

    while len(chiffres) != 0:

        n = i*N

        for c in str(n):

            if c in chiffres:
                chiffres.remove(c)
        i += 1

        if i > 2**32:
            return "INSOMNIA"

    return str(n)
    
for t in range(T):
    N = int(input())
    print "Case #{}: ".format(t+1) + solve(N)
