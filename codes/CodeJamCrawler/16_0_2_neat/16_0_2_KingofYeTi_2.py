import sys

class Solution(object):
  def solve(self,s):
    if not s: return 0
    if len(s) == 1: return s[0] == '-' and 1 or 0
    t = 0
    for i in range(1,len(s)):
      if s[i] != s[i-1]: t += 1
    return s[-1] == '-' and t + 1 or t
     

  def m(self,cases):
    res = []
    sys.stdout = open('2.out','w')
    for i,v in enumerate(cases):
      cur = self.solve(v)
      print('Case #%d: %s' % (i+1,str(cur))) 
    return res

solution = Solution()
num = int(raw_input())
cases = []
for i in xrange(num):
  cases += [str(raw_input())]

solution.m(cases)
