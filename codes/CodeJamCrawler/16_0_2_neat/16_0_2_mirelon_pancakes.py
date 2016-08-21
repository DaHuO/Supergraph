import sys

t = int(sys.stdin.readline())
for i in range(t):
  s = sys.stdin.readline().rstrip('\n')
  r = s[::-1]
  # print(s)
  n = len(s)
  plusy = True
  c = 0
  for a in r:
    if a == '+':
      if plusy:
        continue
      else:
        c += 1
        plusy = True
    else:
      if plusy:
        c += 1
        plusy = False
  print("Case #" + str(i+1) + ": " + str(c))
