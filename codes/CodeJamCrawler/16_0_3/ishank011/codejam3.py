def convert(num, base):
    i=0
    ans=0
    while num>0:
        ans=ans+((base**i)*(num%10))
        num/=10
        i+=1
    return ans

#primes.txt contains all the primes upto 10^8
f=open('primes.txt', 'r').readlines()
f1=open('c1.txt', 'w')
f1.write('Case #1:\n')
f=[int(a[:-1]) for a in f]
g={}
i=0
c=0
while c<500:
    k=1
    l=i
    for j in range(30):
        k=(k*10)+(l%2)
        l/=2
    k=(k*10)+1
    m=[]
    for j in range(2,11):
        print k
        a=convert(k, j)
        for b in f:
            if a%b==0 and a!=b:
                m.append(b)
                break
    if len(m)==9:
        g[k]=m
        c+=1
        f1.write(str(k)+' ')
        for j in range(9):
            f1.write(str(m[j])+' ')
        f1.write('\n')
        print c
    i+=1
print g
f1.close()
        
