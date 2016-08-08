import random
import math
from time import time, clock
def out(n):
  for num in n:
    print(num)
  print('\n')
  
def sort(nums, digit, r):
  buckets = [[] for i in range(r)]
  for num in nums:
    bucket = int((num%(r**digit))//(r**(digit-1)))
    buckets[bucket].append(num)
  return listify(buckets)
  
def LSD_sort(r):
  buckets = sort(a, 0, r)
  for i in range(1, math.ceil(math.log(100, r)) +1):
    buckets = sort(buckets, i, r)
  return buckets

def listify(listy_list): 
  out = []
  for a_list in listy_list:
    out += a_list
  return out
  
    
# {main program}
n=int(input('input n '))
r = 2
a=[]
for i in range(n): a=a+[int(100*random.random())]
print(a)
#out(n)
t=clock()
sorted_list = LSD_sort(r)
out(sorted_list)
print('time ',clock()-t)