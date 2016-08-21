from math import sqrt
from math import ceil
from itertools import count, islice, product
def is_prime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
def getBaseInt(cj,base):
   sum = 0
   for count,value in enumerate(cj):
      sum += int(value)*(base**count)
   return sum
def checkJamCoin(cj):
   N = len(cj)
   baseList = [getBaseInt(cj,base) for base in range(2,11)]
   jamCoinTrue =1
   for baseInt in baseList:
      #print baseInt
      if is_prime(baseInt):
         print baseInt
         jamCoinTrue =0
         break
   if jamCoinTrue == 0:
      return [0]
   else:
      divList=[]
      for baseInt in baseList:
         x = int(ceil(sqrt(baseInt)))
         for divisor in range(2,x):
            if (baseInt%divisor)==0:
               divList.append(str(divisor))
               break               
      return [1] + divList
         
   
filein = open('C:\\sb\\Prog\\Python\\gcg16\\C-small-practice.txt')
fileout = open('C:\\sb\\Prog\\Python\\gcg16\\C-small-practice-out.txt','w')

line = filein.readline()
noOfIter=int(line)
   
for iterNo in range(noOfIter):
   line=filein.readline()
   list1=line.split()
   N=int(list1[0])     #N length jamcoins 
   J=int(list1[1])    #J different jamcoins
   prods = product('01', repeat=N-2)
   cjCount = 0
   print>> fileout, "Case #1:"
   for prod in prods:
      cj=['1']
      cj = cj + list(prod)
      cj.append('1')
      ret = checkJamCoin(cj)
      print ret
      if ret[0] == 1:
         cjCount += 1
         output=[]
         cj.reverse()
         output.append(''.join(cj))
         output = output + ret[1:]
         print ' '.join(output)
         print>> fileout, ' '.join(output)
         if cjCount==J:
            break
   
         
      