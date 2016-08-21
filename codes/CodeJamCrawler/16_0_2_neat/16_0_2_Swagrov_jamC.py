import numpy as np
from math import sqrt
binary_repr = np.binary_repr

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  # code in a limit
  if r>1000000:
    r=1000000
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True  

def check(s):
    for i in range(2,11):
        test = int(s,i)
        if is_prime(test):
            return False
    return True

def getDiv(s):
    r=[]
    for i in range(2,11):
        test = int(s,i)
        if test%2==0:
            r.append('2')
        else:
            d = 3
            # hard code limit
            while test%d != 0 and d<1000000:
                d += 2
            if test%d == 0:
                r.append(str(d))
            else:
                return 'error'
    return ' '.join(r)

N=16
J=50
start = binary_repr(2**(N-1)+1)
valid = []

file=open("small-C_ans.txt",'w')
file.write("Case #1:")
case=start
while len(valid) < J:
    if check(case):
        divs=getDiv(case)
        if divs != 'error':
            valid.append(case)
            file.write('\n'+case+' '+divs)
    case = binary_repr(int(case,2)+2)

file.close()

N=32
J=500
start = binary_repr(2**(N-1)+1)
valid = []

file2=open("large-C_ans.txt",'w')
file2.write("Case #1:")
case=start
while len(valid) < J:
    if check(case):
        divs=getDiv(case)
        if divs != 'error':
            valid.append(case)
            file2.write('\n'+case+' '+getDiv(case))
    case = binary_repr(int(case,2)+2)

file2.close()


