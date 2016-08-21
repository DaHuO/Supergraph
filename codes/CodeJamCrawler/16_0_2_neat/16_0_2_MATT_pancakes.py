#t = int(raw_input())  # read a line with a single integer
#for i in xrange(1, t + 1):
#  s = raw_input().strip()
#  print "Case #{}: {} ".format(i, count_flips(s))

def count_flips(s):
  if s[0] == '+' :
     oc = '-'
  else: 
     oc = '+'
  pos = s[1:].find(oc)+1
  if pos==0 :
     if s[0] == '+' :
        return(0)
     else:
        return(1)
  ns = oc * (pos-1) + s[pos:]
  return(1+count_flips(ns))

def count_flips_alt(s):
  if s.endswith('-'):
     return(1+count_transitions(s))
  else:
     return(count_transitions(s))

def count_transitions(s):
  n = 0
  for i in xrange(1, len(s)):
     if s[i-1] != s[i] :
        n = n+1
  return(n)



 
  

