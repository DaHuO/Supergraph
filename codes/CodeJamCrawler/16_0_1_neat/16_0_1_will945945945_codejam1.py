def f(n):
    n = int(n)
    S = set(list(str(n)))
    i = 0
    k = 0
    while len(S) != 10:
        k += n
        T = set(list(str(k)))
        S = S.union(T)
        i += 1
        if i >= 10**5:
            return 'INSOMNIA'
    return k

F = open('A-large.in')
A = F.read()
A = A.split('\n')[1:-1]
Ans = map(f,A)


E = open('ANS1.large','w')
for i in xrange(len(Ans)):
    E.write('Case #' + str(i+1) + ': ' + str(Ans[i]) + '\n')
E.close()   
