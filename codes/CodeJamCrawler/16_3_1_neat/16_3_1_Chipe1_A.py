tyast=int(input())

def getsum(A):
    return sum([i[0] for i in A])

for sdadsad in range(tyast):
    n=int(input())
    L=[int(x) for x in input().split()]
    atz="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    L=[[L[i],atz[i]] for i in range(len(L))]
    inst=[]
    while getsum(L):
        L.sort()
        s=getsum(L)
        if s == 2:
            inst.append(L[-1][1]+L[-2][1])
            L[-1][0]-=1
            L[-2][0]-=1
        else:
            if L[-1][0]==L[-2][0] and 2*L[-1][0]==s:
                inst.append(L[-1][1]+L[-2][1])
                L[-1][0]-=1
                L[-2][0]-=1
            else:
                inst.append(L[-1][1])
                L[-1][0]-=1
    ans=' '.join(inst)
    print("Case #{}: {}".format(sdadsad+1,ans))
