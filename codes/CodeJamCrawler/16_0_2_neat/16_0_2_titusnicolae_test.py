import fileinput
from itertools import islice

def f(x):
  s = x[0]
  for e in x[1:]:
    if e!=s[-1]:
      s=s+e
  return s
    
if __name__ == "__main__":
  for i, line in enumerate(fileinput.input()):
    if i!=0:
      line = f(line.strip())
      res = len(line)
      if line[-1] == '+':
        res-=1
      print "Case #%d:"%i, res
