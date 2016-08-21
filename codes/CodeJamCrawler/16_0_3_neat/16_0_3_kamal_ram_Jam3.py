def factors(n):
    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return i

        i += w
        w = 6 - w

    return 1
    
fin=open('C-small-attempt0.in','r')
A=fin.readlines()
fin.close()
fout=open('out.out','w')
T=int(A[0])
T=T
for t in range(1,T+1):
    count=0
    N,J=map(int,A[t].strip().split())
    a=(1<<N-1)+1
    b=1<<N
    fout.write('Case #%d:\n' % (t))
    for i in range(a,b,2):
        if count==J:
            break
        F=[0]*9
        j=0
        s=bin(i)[2:]
        flag=True
        for k in range(2,11):
            x=int(s,k)
            f=factors(x)
            if f!=1:
                F[j]=f
                j+=1
            else:
                flag=False
                break
        if flag:
            count+=1
            fout.write(s)
            for f in F:
                fout.write(' ')
                fout.write(str(f))
            fout.write('\n')
fout.close()
