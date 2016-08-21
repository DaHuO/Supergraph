import operator
import random
from fractions import gcd
import decimal
import pickle
def ft(n):
	if n == 2:
		return True
	if not n & 1:
		return False
	return pow(2, n-1, n) == 1
	
def ht(s,i):
  j=len(s)-1
  k=0
  t=0
  while (j>=0):
     k+=(int(s[j]))* (i**t)
     t+=1
     j-=1
  return k
def brent(N):
        if N%2==0:
                return 2
        y,c,m = random.randint(1, N-1),random.randint(1, N-1),random.randint(1, N-1)
        g,r,q = 1,1,1
        while g==1:             
                x = y
                for i in range(r):
                        y = ((y*y)%N+c)%N
                k = 0
                while (k<r and g==1):
                        ys = y
                        for i in range(min(m,r-k)):
                                y = ((y*y)%N+c)%N
                                q = q*(abs(x-y))%N
                        g = gcd(q,N)
                        k = k + m
                r = r*2
        if g==N:
                while True:
                        ys = ((ys*ys)%N+c)%N
                        g = gcd(abs(x-ys),N)
                        if g>1:
                                break
         
        return g
fg = open('out.txt', 'w')    
with open('inp.txt') as f:
    a=[]
    for line in f:
        d = line.split()
        print d
        for i in range(0,len(d)):
            a.append(int(d[i]))
fg.write("Case #1: \n")

n=a[1]
p=a[2]
k=2**(n-1)
f=2**n
if k%2==0:
    k=k+1
while k<f and p>0 :
 s="{0:b}".format(k)
 s=str(s)
 
 if s[0]=='1'  and s[len(s)-1]=='1' :
    m=[]
    h=0
    for i in range(2,11):
        x=ht(s,i)
        if ft(x):
           h+=1    
        m.append(x)
    t=len(m)

    if h==0:
       q=[]
      # q.append(s);
       u=0
       for j in range(0,len(m)):
           d=m[j]
           l=3
           while l<=100:
               if d%l==0:
                   u+=1
                   q.append(l)
                   break
                 
               l+=2
       if u==len(m):
            p=p-1
            #print p
            w=""
            w+=s+" "
            for i in q:
               w+=str(i)+" "
            w+="\n"  
            fg.write(w)
                
                  
 k+=2
print p 
   
	
