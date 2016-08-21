import sys

T = input()
for t in range(1, T +1):
  line = sys.stdin.readline().strip()
  while len(line) > 0 and line[-1] == '+': line = line[:-1]
  ans = 0
  for i in range(0, len(line)):
    if line[i] != line[i-1] or i == 0: ans += 1
  print('Case #%d: %d' % (t, ans))
