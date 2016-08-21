import sys
sys.setrecursionlimit(10000)

def findMax(s):
  j = 0
  for i,a in enumerate(s):
    if a >= s[j]:
      j = i
  return j

def solve(s):
  if len(s) == 0:
    return ""
  l = findMax(s)
  return s[l] + solve(s[:l]) + s[l+1:]

t = int(sys.stdin.readline())
for i in range(t):
  s = sys.stdin.readline().rstrip('\n')

  print("Case #" + str(i+1) + ": " + solve(s))