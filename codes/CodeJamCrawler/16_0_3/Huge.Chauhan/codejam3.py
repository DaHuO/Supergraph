from math import sqrt
def d(num):
    for i in range(2,int(num/2)+1):
        if num % i == 0:
            return i
def isp(num):
    if num > 1:
       for i in range(2,int(sqrt(num))):
         if (num % i) == 0:
           return 0
    else:
        return 0
    return 1
def b10toN(nu,base):
    cs, mods = "",""
    curren = nu
    while curren:
        mo = curren % base
        curren = curren // base
        cs = chr(48 + mo + 7*(mo > 10)) + cs
    return cs
def bToN(num,base):
    r=0
    j=len(num)-1
    for i in range(len(num)):
        r+=int(num[i])*pow(base,j)
        j-=1
    return r
U=eval(input())
for j in range(1,U+1):
   inp=list(map(int,input().split()))
   v=inp[1]
   print("Case #{}:".format(j))
   for i in range(2**(inp[0]-1),2**inp[0]):
      y= b10toN(i,2)
      if y[-1]=='1' and y[0]=='1':
           c=[]
           z=int(y)
           c.append(z)
           for k in range(2,11):
             z=bToN(y,k)
             if isp(z):
                 c=[]
                 break
             else:
                 c.append(d(z))
           if c==[]:
               continue
           else:
              if v==0:
                  exit
              else:
                  v-=1
                  for q in c:
                      print(q, end=" ")
                  print()
