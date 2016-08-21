'''
Created on 30. 4. 2016

@author: Vendula Poncova
'''

import sys
import string

def main():
  
  t = int(input())  # read a line with a single integer
  
  for case in range(1, t + 1):
    
    n = int(input())
    parties = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    
    a, b, ai, bi = -1, -1, -1, -1
    
    for i in range(n):

      if parties[i] > bi :
        if parties[i] > ai :
          b, bi = a, ai
          a, ai = i, parties[i]
        else :
          b, bi = i, parties[i]  
        
    #rint(a,ai,b,bi)
    
    print("Case #{}:".format(case), end="")
    
    for i in range(ai - bi) :
      print(" {}".format(string.ascii_uppercase[a]), end="")
    
    for i in range(n):
      if i != a and i != b :
        for j in range(parties[i]) :
          print(" {}".format(string.ascii_uppercase[i]), end="")

    for i in range(bi) :
      print(" {}{}".format(string.ascii_uppercase[a],string.ascii_uppercase[b]), end="")
    

    print("")

if __name__ == '__main__':
      main()