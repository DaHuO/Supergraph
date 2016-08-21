__author__ = 'Vinayak'

import math,sys,random

range1 = lambda start, end: range(start, end+1)

def is_probable_prime(n, k = 7):
   """use Rabin-Miller algorithm to return True (n is probably prime)
      or False (n is definitely composite)"""
   if n < 6:  # assuming n >= 0 in all cases... shortcut small cases here
      return [False, False, True, True, False, True][n]
   elif n & 1 == 0:  # should be faster than n % 2
      return False
   else:
      s, d = 0, n - 1
      while d & 1 == 0:
         s, d = s + 1, d >> 1
      # Use random.randint(2, n-2) for very large numbers
      for a in random.sample(range(2, min(n - 2, sys.maxsize)), min(n - 4, k)):
         x = pow(a, d, n)
         if x != 1 and x + 1 != n:
            for r in range(1, s):
               x = pow(x, 2, n)
               if x == 1:
                  return False  # composite for sure
               elif x == n - 1:
                  a = 0  # so we know loop didn't continue to end
                  break  # could be strong liar, try another a
            if a:
               return False  # composite if we reached end of this loop
      return True  # probably prime if reached end of outer loop

def is_six_prime(a):
    return (a-1)%6==0 or (a+1)%6==0

def is_prime(a):
    if not is_six_prime(a):
        return False
    elif not is_probable_prime(a):
        return False
    else:
        return True

def get_first_factor(num):
    #print(num)
    if (num%2==0):
        #print(2)
        return 2
    if (num%3==0):
        #print(3)
        return 3
    for i in range(1,10**5):
        if (num%(6*i+1))==0:
            #print(6*i+1)
            return (6*i+1)
        if (num%(6*i-1))==0:
            #print(6*i-1)
            return (6*i-1)
    else:
        #print(-1)
        return -1

data=list()
output_data=''

with open("C-large.in",'r') as f:
    for line in f.readlines():
        data.append(line)


test_case=int(data.pop(0))
i=0
while i<test_case:
    output_data+="Case #"+str(i+1)+":\n"
    temp=data.pop(0).split(" ")
    N=int(temp[0])
    J=int(temp[1])
    num_stack=set()
    str_list=["1"]
    for t in range(N-2):
        str_list.append("0")
    num=int("".join(str_list),2)
    #print("{0:b}".format(num+2))
    while len(num_stack)<J :
        primality=False
        str_num="{0:b}".format(num)
        str_num+="1"
        for m in range(2,11):
            #print(int(str_num,m),is_prime(int(str_num,m)))
            #print(m,int(str_num,m),sep=" ")
            if (is_prime(int(str_num,m))):
                primality=True
                break
        #print(num)
        #print(primality)
        if not primality:
            second_primality_check=False
            factor_list=[]
            #print("here1")
            for m in range(2,11):
                temp=str(get_first_factor(int(str_num,m)))
                if temp == "-1":
                    second_primality_check=True
                    #print("second")
                    break
                factor_list.append(temp)
            #print("here2")
            #print(len(factor_list))
            if not second_primality_check:
                output_data+=str_num+" "+" ".join(factor_list)+"\n"
                num_stack.add(str_num)
            #print(len(num_stack))
        #print(num_stack)
        num=num+1
    i=i+1



#print(output_data)
with open("outputfile.in",'w') as f:
    f.write(output_data)