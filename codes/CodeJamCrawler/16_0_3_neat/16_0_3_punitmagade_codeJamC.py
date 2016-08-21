import itertools
import math
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))
f=open('input.in','r')
fout=open('output.out','w')
t=f.readline()
N,J=map(int,f.readline().strip().split())
li=["".join(seq) for seq in itertools.product("01", repeat=14)]
n=len(li)
i=0
fout.write('Case #1:\n')
while i<n and J>0:
    s='1'+li[i]+'1'
    j=2
    flag=1
    l=[]
    while j<11 and flag:
        num=int(s,j)
        if not is_prime(num):
            k=2
            while k<num/2:
                if num%k==0:
                    l.append(k)
                    break
                k+=1
        else:
            flag=0
        j+=1
    if flag==1:
        temp=s
        for p in range(len(l)):
            temp=temp+' '+str(l[p])
        temp+='\n'
        fout.write(temp)
        #print temp
        J-=1
    i+=1
fout.close()
f.close()
