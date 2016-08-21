from collections import Counter
from itertools import count
import fileinput

def digits(x):
  return map(int, str(x))

def f(x):
  if x==0: 
    return -1
  digits_counter = set()
  n = 0
  for j in count(x, x):
    n+=1
    digits_counter |= set(digits(j)) 
    if digits_counter == set(range(10)):
      return j

if __name__ == "__main__":
  for i, line in enumerate(fileinput.input()):
    if i!=0:
      res = f(int(line))
      print "Case #%d:"%i, res if res!=-1 else "INSOMNIA"
