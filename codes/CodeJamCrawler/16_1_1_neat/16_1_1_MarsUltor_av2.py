from lcj import *
with openw() as g:
 def f(s):
  r=s[0]
  for c in s[1:]:
   r=c+r if c>=r[0]else r+c
  return r
 for line in lines('A'):
  case(g,f(line))