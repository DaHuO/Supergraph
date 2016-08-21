from sys import stdin

def solve(S):
  prev = ""
  count = 0
  for c in S:
    if c != prev:
      count += 1
      prev = c
  if prev == '+':
    count -= 1
  return count

T = int(stdin.readline())
for tc in range(1, T+1):
  print "Case #%d: %s" % (tc, solve(stdin.readline().strip()))
