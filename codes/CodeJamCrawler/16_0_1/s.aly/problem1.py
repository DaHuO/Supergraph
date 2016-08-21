##t = int(input())
##for i in range(1, t + 1):
##  n = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
##  print("Case #{}: {}".format(i,n))
##  # check out .format's specification for more formatting options


from collections import deque

def magic(num):
        digits = deque()
        while True:
            num,r = divmod(num,10)
            digits.appendleft(r)
            if num == 0:
                break
        return set(digits)

t = int(input())
for i in range(1, t + 1):
  r = set([0,1,2,3,4,5,6,7,8,9])
  y = int(input())  # read a list of integers, 2 in this case
  z=0
  n=0
  while len(r)!=0 and z<=100:
      z=z+1
      n=z*y
      dig = magic(n)
      r=r-dig
  if z>=100:
      n="INSOMNIA"    
  print("Case #{}: {}".format(i,n))
  
