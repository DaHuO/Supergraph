def solve(n):
    sol = []
    d = 1

    S = n[0]
    for i in range(len(n)-1):
        S = S + n[i+1]
    S = sorted(S)
    for i in range(len(S)):
        count = S.count(S[i])
        if round(count/2) != count/2:
            sol.append(S[i])

    S1 = set(sol)

    T = list(S1)
    out1 = sorted(T)



    return d, out1



IN = open('input.txt', 'r')
OUT = open('output.txt', 'w')

T = int(IN.readline())

for line in range(T):
    # Instanz mit mehreren Zeilen
    yes = 1
    if yes == 0:
        #sizen = int(IN.readline())
        n = list(map(int, IN.readline().split()))
    else:
        T0 = int(IN.readline())
        n = []
        for i in range(2*T0-1):
            n.append(list(map(int, IN.readline().split())))

    if solve(n)[0] == 1:
        answer = ' '.join(map(str,solve(n)[1]))
        OUT.write('Case #{}: {}\n'.format(line + 1, answer))
    else:
        OUT.write('Case #{}:\n'.format(line + 1))
        for i in range(len(solve(n)[1])):
            answer = ' '.join(map(str,solve(n)[1][i]))
            OUT.write('{}\n'.format(answer))
    if yes == 1:
        line -= T0
IN.close()
OUT.close()