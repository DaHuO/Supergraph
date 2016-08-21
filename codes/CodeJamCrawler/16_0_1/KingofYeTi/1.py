import sys

class Solution(object):
  def solve(self,n):
    d = [False] * 10 
    t = 0
    for i in xrange(1,101):
      cur = str(n * i)
      for m in cur:
        c = ord(m) - ord('0')
        if d[c] == False:
          t += 1
          d[c] = True
      if t == 10:
        return i*n
    return "INSOMNIA"

  def m(self,cases):
    res = []
    sys.stdout = open('1.out','w')
    for i,v in enumerate(cases):
      cur = self.solve(v)
      print('Case #%d: %s' % (i+1,str(cur))) 
    return res

solution = Solution()
num = int(raw_input())
cases = []
for i in xrange(num):
  cases += [int(raw_input())]

solution.m(cases)
