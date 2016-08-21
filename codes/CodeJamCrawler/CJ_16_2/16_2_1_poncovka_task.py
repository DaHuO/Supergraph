'''
Created on 30. 4. 2016

@author: Vendula Poncova
'''

import string

def print_digit(digit, n):
  for _ in range(0,n):
    print(digit, end="")

def main():
  
  t = int(input())  # read a line with a single integer
  
  for i in range(1, t + 1):
    
    D = {digit : 0 for digit in string.ascii_uppercase}
    
    for l in input():
      D[l] = D[l] + 1 
    
    A = [0] * 10
    A[0] = D["Z"]
    A[2] = D["W"]
    A[4] = D["U"]
    A[6] = D["X"]
    A[8] = D["G"]
    
    A[1] = D["O"] - A[0] - A[2] - A[4]
    A[3] = D["H"] - A[8]
    A[5] = D["F"] - A[4]
    A[7] = D["V"] - A[5]
    A[9] = D["I"] - A[5] - A[6] - A[8]
    
    print("Case #{}: ".format(i), end="")
    
    for digit in range(0,10) :
      for _ in range(0,A[digit]):
        print(digit, end="")
    
    print()
    #print(D)

if __name__ == '__main__':
      main()
