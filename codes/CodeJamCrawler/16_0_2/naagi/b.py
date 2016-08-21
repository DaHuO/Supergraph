import sys

tests = input()
for test in range (tests):
  s = sys.stdin.readline().strip() + '+'
  res = s.count('+-') + s.count('-+')
  print ("Case #" + str(test + 1) + ": " + str(res))
