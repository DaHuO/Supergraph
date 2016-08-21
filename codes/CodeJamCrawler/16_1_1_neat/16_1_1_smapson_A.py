import sys
sys.setrecursionlimit(1500)

def last_word(s):
  if s == "": 
    return ""
  n = len(s)
  first_letter = max(range(n), key=lambda x: (s[x],x))
  return s[first_letter] + last_word(s[:first_letter]) + s[first_letter+1:]

T = int(raw_input())
for test_case in range(T):
  s = raw_input()
  print "Case #%s: %s"%(test_case+1, last_word(s))
