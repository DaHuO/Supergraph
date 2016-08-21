T=int(input())
for loop in range(T):
    K,C,S=map(int,input().split(" "))
    if K==S:
        print("Case #"+str(loop+1)+":",end=" ")
        for i in range(1,K+1):
            print(i,end=" ")
    else:
        X=K**C
        M=K
        print("Case #"+str(loop+1)+":",end=" ")
        print(K-1,end=" ")
        while M<X:
            M=M*C
            print(M)
    print("")
