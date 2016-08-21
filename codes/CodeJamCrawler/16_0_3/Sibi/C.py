import sys
from math import sqrt

iFile = open(sys.argv[1],"r")

T = int(iFile.readline().strip())

for t in range(T):
    line = iFile.readline().strip().split()
    
    N = int(line[0])
    J = int(line[1])
    
    minBin = '1'+(N-2)*'0'+'1'
    
    print("Case #"+str(t+1))
    
    coin = minBin
    
    for j in range(J):
      while True:
        out = coin
        for base in range(2,11):
          test = int(coin,base)
          for div in range(2,int(sqrt(test))+1):
            if test%div == 0:
              out += ' '+str(div)
              break
          else:
            break
        else:
          print out
          coin = "{0:b}".format(int(coin,2) + 2)
          break
          
        coin = "{0:b}".format(int(coin,2) + 2)
      
