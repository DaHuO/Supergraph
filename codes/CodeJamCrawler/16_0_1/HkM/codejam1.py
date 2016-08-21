def codejam1(N):
    L=[];
    i=1;
    while len(L)<10:
        if i>10000:
            return ("INSOMNIA");
        T=list(str(i*N));
        for j in range(len(T)):
            if T[j] not in L:
                L.append(T[j]);
        i+=1;
    return(N*(i-1));
k=1;
n=input();
I=[];
while k<=n:
    I.append(input());
    k+=1;
m=1;
while m<=n:
    print 'Case #' +str(m)+': '+str(codejam1(I[m-1]));
    m+=1;

