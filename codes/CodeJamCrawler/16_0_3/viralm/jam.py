def is_prime(x):
    if x==2:
        return -1
    i=3
    while i*i<=x:
        if x%i==0:
            return i
        i+=2
    return -1
ttt=input()
n,J=(int(i) for i in raw_input().split())
num_min=1+2**(n-1)
num_max=(2**n)-1
l=[]
count=0
print "Case #1:"
for i in xrange(num_min,num_max+1,2):
    if count==J:
        break
    temp=bin(i)[2:]
    ans=0
    flag=True
    l=[]
    for j in range(2,11):
        p=1
        ans=0
        for k in range(n-1,-1,-1):
            #print "ans =",ans
            ans+=p*int(temp[k])
            p=p*j
        z=is_prime(ans)
        if z!=-1:
            l.append([ans,z])
        else:
            flag=False
            break
    if flag==True:
        count+=1
        #print 'l =',l
        print bin(l[0][0])[2:],
        for c in l:
            print c[1],
        print
