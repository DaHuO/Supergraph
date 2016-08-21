#!/usr/bin/python
class TBD:
  Per = []
  def isPrime(self,n):
    if n <= 1:
      return False
    i=2
    while i*i<=n:
      if n%i==0:
        return i
      i+=1
    return 0
  
  def C(self,a,n):
    if n==0:
      return 1
    return a*self.C(a,n-1)
    
  def P(self,str1,l,L):
    #print(str1,l)
    if len(str1)==L:
      self.Per.append(str1)
    else:
      self.P(str1+'0',l+1,L)
      self.P(str1+'1',l+1,L)
      
  def str1ToNum(self, str1, B):
    R = 0
    index = len(str1)
    for i in str1:
      index = index - 1
      n = int(i)
      if n == 1:
        R = R + self.C(B,index)
    return R
    
  def G(self,n,j):
    #permutation to get internal str1ing, self.Per
    self.P('',0,n-2)
    #print(self.Per)
    count = 0
    for s in self.Per:
      str1 = '1'+ s + '1'
      Flag = True
      R = []
      for i in range(9):
        num = self.str1ToNum(str1,i+2)
        yinzi = self.isPrime(num)
        if yinzi == 0:
          Flag = False
          break
        else:
          R.append(yinzi)
      if Flag:
        str12 = " ".join(str(x) for x in R)
        print("Case #1:")
        print("%s %s"%(str1,str12))
        count = count + 1
        if count == j:
          return
        
tbd=TBD()
tbd.G(16,50)
