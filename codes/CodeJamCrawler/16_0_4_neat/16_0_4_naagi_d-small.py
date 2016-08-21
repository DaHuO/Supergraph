import sys


def getnum(a, k):
  num = 0
  for i in a:
    num = num * k + i
  return num

tests = input()
for test in range (tests):
  k, c, s = map (int, sys.stdin.readline().split())
  if s < k - c + 1:
    res = 'IMPOSSIBLE'
  else:
    res = " ".join(map (str, range (1, k+1)))
  print ("Case #" + str(test + 1) + ": " + str(res))
  