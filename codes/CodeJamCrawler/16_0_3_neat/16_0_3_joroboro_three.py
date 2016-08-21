from __future__ import print_function
import sys
from pprint import pprint
from math import sqrt
N = 32
J = 500
#N = 6
#J = 3
def main():
    print("Case #1: ")
    start = 2**(N-1)
    numbers = []
    while( len(numbers) != J ):
       start = start + 1
       binary = str(bin(start))[2:]
       if int(binary) % 2 == 0:
           continue
       baseNums = []
       for base in range(2,11):
           temp = int(binary,base)
           for i in range(2,1000):
               if temp % i == 0:
                   baseNums.append(i)
                   #print "In base ", str(base), " devisable by ", str(i)
                   break
           if len(baseNums) != base - 1:
                break
       if len(baseNums) != 9:
           #print("Not ", str(binary))
           continue
       print(binary, end=' ')
       numbers.append(binary)
       for num in baseNums:
           print(num, end=' ')
       print() 
main()
