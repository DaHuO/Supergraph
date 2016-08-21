f=open("A-large.in")
r=f.read().split('\n');
f.close();

f=open("anscsheep.txt","w")
n=int(r[0])

lst=[0,1,2,3,4,5,6,7,8,9]
r.remove(r[0])
r.pop()
sl=[]
print(r)
for i in r:
 sl.append(int(i))
 
print(sl)
 

for i in range(n):
 
 k=sl[i]
 if(k==0):
  aa='''Case #'''+str(i+1)+''': INSOMNIA\n'''
  f.write(aa)
  continue;
  
 number=[]
 s=1
 flag=0;
 while(flag!=1):
  num=k*s
  res=num
  s=s+1
  
  while(num):
   r=num%10
   if r not in number:
    number.append(r)
    number.sort()
    
   num=num//10
   
   
  if(lst==number):
   aa='''Case #'''+str(i+1)+''': '''+str(res)+'''\n'''
   f.write(aa)
   flag=1
         
f.close()   
    
   
  
 
 
