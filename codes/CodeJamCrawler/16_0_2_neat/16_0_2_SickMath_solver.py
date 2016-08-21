f = open('B-small.in')
g = open('small.out', 'w')

T = int(f.readline()[:-1])

for case in range(T) :
    L = f.readline()[:-1]
    L = [0 if i == '-' else 1 for i in L]
    m = 0
    while True :
        while len(L) > 0 and L[-1] == 1 :
            L = L[:-1]
        if len(L) == 0 :
            break
        tm = len(L) if L[0] == 0 else L.index(0)
        F = [0 if i == 1 else 1 for i in L[:tm]]
        F.reverse()
        L = F + L[tm:]
        m += 1
    res = m
    output = 'Case #' + str(case+1) + ': ' + str(res)
    print(output)
    g.write(output + '\n')

f.close()
g.close()
