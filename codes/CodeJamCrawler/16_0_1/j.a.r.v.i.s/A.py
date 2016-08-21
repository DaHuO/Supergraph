T=int(input())
for x in range(T):
    caseNum=str(x+1)
    N=int(input())
    S=set()
    default=set([0,1,2,3,4,5,6,7,8,9])
    if N == 0:
        print("Case #"+caseNum+":","INSOMNIA")
        continue
    for i in range(1,10000000000):
        N1=i*N
        numTemp=str(N1)
        for ch in numTemp:
            S.add(int(ch))
        if S == default:
            break
    print("Case #"+caseNum+":",N1)