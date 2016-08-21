from math import sqrt
def b10toN(number,base):
    converted_str = ""
    currentnum = number
    while currentnum:
        mod = currentnum % base
        currentnum = currentnum // base
        converted_str = chr(48 + mod + 7*(mod > 10)) + converted_str
    return converted_str
def isprime(number):
    if number > 1:
       for i in range(2,int(sqrt(number))):
         if (number % i) == 0:
           return 0
    else:
        return 0
    return 1
def bToN(number,base):
    ans=0
    j=len(number)-1
    for i in range(len(number)):
        ans+=int(number[i])*pow(base,j)
        j-=1
    return ans
def divisor(z):
    for i in range(2,int(z/2)+1):
        if z % i == 0:
            return i
T=int(input())
for i in range(1,T+1):
   x=list(map(int,input().split()))
   v=x[1]
   print("Case #{}:".format(i))
   for j in range(2**(x[0]-1),2**x[0]):
      y= b10toN(j,2)
      if y[0]=='1' and y[-1]=='1':
           z=int(y)
           res=[]
           res.append(z)
           for k in range(2,11):
             z=bToN(y,k)
             if isprime(z):
                 res=[]
                 break
             else:
                 res.append(divisor(z))
           if res == []:
               continue
           else :
              if v==0:
                  exit
              else:
                  v-=1
                  for q in res:
                      print(q, end=" ")
                  print()
