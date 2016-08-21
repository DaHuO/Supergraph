filename  = "B-large.in"
f = open(filename,'r')
out = open("output.out",'w')
T =int(f.readline())
for Ca in range(T):
    [N,K]=[int(j) for j in f.readline().split()]
    P =[float(j) for j in f.readline().split()]
    P = sorted(P)
    #print([K,P])
    maxi =-1.0
    for l in range(K+1):
        Pneu=P[0:l]+P[N-K+l:]
        #print("Pneu"+str(Pneu))
        Y=[0]*(K+1)
        Y[0]=1
        #print("Probs")
        #print(Y)
        for p in Pneu:
            Y=[Y[0]*(1-p)]+[p*Y[i-1]+(1-p)*Y[i] for i in range(1,len(Y))]
            #print(Y)
        #print("Final Prob:"+str(Y[len(Y)//2]))
        maxi  = max(maxi,Y[len(Y)//2])
    print("Case #"+str(Ca+1)+": "+'{:.20f}'.format(maxi))
    out.write("Case #"+str(Ca+1)+": "+'{:.20f}'.format(maxi)+"\n")
f.close()
out.close()
