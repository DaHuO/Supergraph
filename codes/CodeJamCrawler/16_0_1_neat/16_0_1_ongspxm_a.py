N = input()
for n in range(N):
    x = input()
    if not x:
        print 'Case #%d: INSOMNIA'%(n+1)
    else:
        C = []
        X = 0

        while len(C)<10:
            X += x
            for c in str(X):
                C += [c]
            C = list(set(C))

        print 'Case #%d: %d'%(n+1, X)

