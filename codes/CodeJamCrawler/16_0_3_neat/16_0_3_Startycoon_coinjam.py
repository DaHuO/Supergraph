import itertools
import math


def baseN(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and  "0" ) or ( baseN(num // b, b).lstrip("0") + numerals[num % b])



def isprime(num):
 num1=int(num**0.5)
 for i in range(2,num1+1):
  if(num%i==0):
   return(i)
   
 return(-1)



f=open("C-small-attempt0.in")
r=f.read().split('\n')
f.close()
f=open("anscoinjam.txt","w")
r.remove(r[0])
s=r[0].split(" ")
n=int(s[0])
j=int(s[1])
lst1 = [list(i) for i in itertools.product([0, 1], repeat=n)]
lst=[]
fact=[]
for i in lst1:
 if(i[0]==1 and i[-1]==1):
  ti=i;
  ti.reverse()
  ii=0
  fac=[]
  stt=""
  
  for ff in ti:
   stt=stt+str(ff)
   
  su=stt

  flag=0
  for jj in range(2,11):
   if(flag==1):
    jj=11
   elif(flag!=-1):
    ss=int(su,jj)
    print("ss:"+str(ss))
    an=isprime(ss)
    print("fact"+str(an))
    if(an==-1):
     flag=1
     continue
    
    else:
     fac.append(an)
     
   else:
    pass
      
  if(flag==0):
   fact.append(fac)
   print(i)
   lst.append(i)
   
  if(len(lst)==j):
   break
    
   
ii=0  
aa='''Case #1:\n'''
f.write(aa)

for i in lst:
 res=""
 for kk in i:
  res=res+str(kk)
  
 
 for ff in fact[ii]:
  res=res+" "+str(ff)
  
 ii=ii+1
  
 aa=res+'''\n'''
 f.write(aa)
 
 
 
   
   


f.close()
