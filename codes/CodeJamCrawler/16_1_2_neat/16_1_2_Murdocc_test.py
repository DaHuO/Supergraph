test=int(raw_input())


for ha in range(test):
    n=int(raw_input())
    m=dict()
    for i in range(2*n-1):
        s=raw_input()
        s=s.split()
        print s
        s=map(int,s)
        for j in s:
            if(j in m):
                m[j]+=1
            else:
                m[j]=1

    print 'Case #'+str(ha+1)+':',
    for i in m:
        if(m[i]%2==1):
            print i,




