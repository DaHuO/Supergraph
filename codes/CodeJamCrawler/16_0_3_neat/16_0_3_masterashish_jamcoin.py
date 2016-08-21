#!/usr/bin/python

import itertools
import sys

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
#    print '\t',f
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True

def gcd(x, y):
   if x == 0:
        return y

   else:
        return gcd(y%x, x)
 
testcase = input()
n,j = raw_input().split()
n = int(n)
j = int(j)

print "Case #1:"

lst = list(itertools.product([0, 1], repeat= n))

new_lst = [item for item in lst if ( (item[0] != 0) and (item[-1] != 0) ) ]

#print new_lst
count = 0
for item in new_lst:
    check = 0
    for i in range(2, 11):
       num = 0  
       for x in range(0, n):
           num = num + (i**(n - x - 1)) * item[x]
#       print item ,i, num

       if is_prime(num):
            break;
       else:
            check = check + 1
    if check == 9: 
       sys.stdout.write(''.join(str(i) for i in item))
       sys.stdout.write(' ')
       count = count + 1

#       print ''.join( str(i) for i in item) 
       for i in range(2,11):
            num = 0
            for x in range(0, n):
                num = num + (i**(n - x - 1)) * item[x]
            a = 2
            while(1):
                if gcd(a, num) > 1:
                    sys.stdout.write(str(a))
                    sys.stdout.write(' ')
                    break;
                a = a+1
       print
#    print "count = ", count
    if count >= j:
       exit()
