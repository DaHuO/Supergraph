import itertools
import math

def getDivisor(x):
  s = math.floor(math.sqrt(x))
  for y in range(2, s + 1):
    if x % y == 0 :
      return y
  return 1

def genCoins(n, j):
  for i in itertools.product([0,1],repeat=(n - 2)):
  
    divs = []
    for b in range(2, 11):
      x = 1 + b**(n-1)
      m = n - 2
      for d in i :
        x = x + d*b**m
        m = m - 1
        
      d = getDivisor(x)
      
      if d == 1 :
        break
      else :
        divs.append(d)
        
    if len(divs) == 9 :
      print("%d %s" % (x, " ".join([str(d) for d in divs])))
    
      j = j - 1
      if j == 0 :
        return
       

with open("C-small-attempt0.in") as f :
  t = f.readline()
  t = int(t)
  for i in range(t) :
    case = f.readline()
    n, j = case.strip().split()
    n, j = int(n), int(j)

    print("Case #1:")
    genCoins(n, j)
