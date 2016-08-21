def solve2(k,c):
  if(c==1 or k==1):
    return range(1,k+1)
  
  ss  = k**(c-1)
  sss = k**(c-2)
  
  cur = 1+ss-sss
  
  ans = []
  for x in xrange((k+1)/2):
    ans.append(cur)
    cur+=ss-sss
  return ans
    

def solve():
  k,c,s = map(int,raw_input().split())
  n = solve2(k,c)
  #~ print n
  if(len(n)<=s):
    return ' '.join(map(str,n))
  else:
    return 'IMPOSSIBLE'


t = int(raw_input())
for x in xrange(1,t+1):
  print 'Case #%d: %s'%(x,solve())
  

#~ abcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg
