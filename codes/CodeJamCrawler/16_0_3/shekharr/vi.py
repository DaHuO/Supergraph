from math import sqrt
def base10toN(num,base):
    converted_string, modstring = "", ""
    currentnum = num
    while currentnum:
        mod = currentnum % base
        currentnum = currentnum // base
        converted_string = chr(48 + mod + 7*(mod > 10)) + converted_string
    return converted_string
def isprime(num):
    if num > 1:
       for i in range(2,int(sqrt(num))):
         if (num % i) == 0:
           return 0
    else:
        return 0
    return 1
def binaryToN(num,base):
    result=0
    j=len(num)-1
    for i in range(len(num)):
        result+=int(num[i])*pow(base,j)
        j-=1
    return result
def divisor(z):
    for i in range(2,int(z/2)+1):
        if z % i == 0:
            return i
t=eval(input())
for j in range(1,t+1):
   x=list(map(int,input().split()))
   v=x[1]
   print("Case #{}:".format(j))
   for i in range(2**(x[0]-1),2**x[0]):
      y= base10toN(i,2)
      if y[0]=='1' and y[-1]=='1':
           z=int(y)
           a=[]
           a.append(z)
           for k in range(2,11):
             z=binaryToN(y,k)
             if isprime(z):
                 a=[]
                 break
             else:
                 a.append(divisor(z))
           if a == []:
               continue
           else :
              if v==0:
                  exit
              else:
                  v-=1
                  for q in a:
                      print(q, end=" ")
                  print()
