def makesmaller(A):
    if len(A)==1:
        return A
    else:
        l =len(A)//2
        L = makesmaller(A[:l])
        R = makesmaller(A[l:])
        return min(L+R,R+L) 

filename  = "A-large.in"
f = open(filename,'r')
out = open("output.out",'w')
T =int(f.readline())
for Ca in range(T):
    [N,R,P,S]=[int(j) for j in f.readline().split()]
    k=int((P+R-S)/2)
    #print([N,P,R,S,k])
    ret=""
    for i in range(N):
        k=(P+R-S)/2
        #print([P,R,S])
        [P,R,S]  = [k,R-k,P-k]
        if (P<0) or (R<0) or (S<0):
            ret ="IMPOSSIBLE"
            break
    if ret!="IMPOSSIBLE":
        ret = "P"*int(P)+"R"*int(R)+"S"*int(S)
        for i in range(N):
            ret =ret.replace("P","pr").replace("R","rs").replace("S","sp")
            ret=ret.replace("r","R").replace("s","S").replace("p","P")
        #print(ret)
        ret = makesmaller(ret)
    print("Case #"+str(Ca+1)+": "+ret)
    out.write("Case #"+str(Ca+1)+": "+ret+"\n")
f.close()
out.close()
