import sys

def sort (s):
  n = len(s)
  if n <= 1:
    return s
  s1 = sort(s[:n/2])
  s2 = sort(s[n/2:])
  if s1 < s2:
    return s1 + s2
  else:
    return s2 + s1

tests = input ()
for test in range (tests):
  n, r, p, s = map (int, sys.stdin.readline().split())
  res = 'IMPOSSIBLE' 
  for winner in ('R', 'P', 'S'):
    lineup = winner
    for i in range (n):
      lineup = lineup.replace('R', 'rs')
      lineup = lineup.replace('S', 'ps')
      lineup = lineup.replace('P', 'pr')
      lineup = lineup.upper()
    lineup = sort (lineup)
    if lineup.count ('R') <= r and lineup.count ('P') <= p and lineup.count ('S') <= s:
      if res == 'IMPOSSIBLE' or res > lineup:
        res = lineup
  print ("Case #" + str(test + 1) + ": " + str(res))
