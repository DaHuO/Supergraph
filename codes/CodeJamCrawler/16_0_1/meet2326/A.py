T = int(input())
for i in range(T):
    N = int(input())
    if(N == 0):
        print("Case #{}: {}".format(i + 1,"INSOMNIA"))
    else:
        count, Nd = 0, 0
        M = [0] * 10
        while count != 10:
            Nd += N
            D = [int(j) for j in str(Nd)]
            for d in D:
                if(M[d] != 1):
                    M[d] = 1
                    count += 1
        print("Case #{}: {}".format(i + 1, Nd))     