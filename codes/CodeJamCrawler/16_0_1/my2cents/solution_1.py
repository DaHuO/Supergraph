for t in range(int(input())):       # First input is the number of cases.
    N = int(input())                # S is the starting number
    if N == 0:
        print ("Case #%d: %s"%(t+1, 'INSOMNIA'))
    else:
        temp = N
        S = set([int(i) for i in str(temp)])
        F = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
        while not(S.issuperset(F)):
            temp = temp + N
            S = S.union([int(i) for i in str(temp)])
        print("Case #%d: %d"%(t+1, temp))
        
