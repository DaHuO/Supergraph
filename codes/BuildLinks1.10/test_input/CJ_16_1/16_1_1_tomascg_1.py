


def solve(S):
    init = S[0]
    biggestSeen= S[0]
    for i in range(1,len(S)):
        if S[i] >= biggestSeen:
            init = S[i] + init
            biggestSeen = S[i]
        else:
            init = init + S[i]
    return init
        

f = open('a.in', 'r')
g = open('a.out', 'w')

t = int(f.readline())

for i in range(1,t+1):

    #read input
    S = f.readline().split('\n')[0]
    

    #solve
    ans = solve(S)
    pr = "Case #"+str(i)+ ": " + str(ans)
    print pr
    g.write(pr+ '\n')


f.close()
g.close()
