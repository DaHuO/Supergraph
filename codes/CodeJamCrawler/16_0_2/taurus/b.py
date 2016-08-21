import math
import random
    
def main():
  testcases = int(input())
  for caseNr in range(1, testcases+1):
    s = input()
    print("Case #%i: %i" % (caseNr, solve(s)))
    
def solve(string):
  
  s = string
  iterations = 0
  
  while True:
    # check if ok
    if "-" not in s:
      break
    if "+" not in s:
      iterations += 1
      break
    
    # find where to start to flip
    c = s[-1]
    j = 0
    
    for j in range(len(s) - 1, -1, -1):
      if s[j] != c:
        break
     
    if s[0] == c:
      c2 = s[j]
      l = j
      for j in range(l, -1, -1):
        if s[j] != c2:
          break
    
    s = flip(s, j)      
    
    iterations += 1
  
  return iterations
    
def flip(s, j):
  t = s[:j+1]
  t = t[::-1]
  t = changeSign(t)
  return t + s[j+1:]

def changeSign(s):
  res = ""
  for c in s:
    if c == '+':
      res += '-'
    else:
      res += '+'
  return res

if __name__ == "__main__":
  main()
    