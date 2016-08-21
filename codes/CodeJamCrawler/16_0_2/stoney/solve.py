INPUT_FILE = "in.txt"

entries = []
with open(INPUT_FILE, 'r') as fin:
  for raw_line in fin.readlines():
    entries += [[x for x in raw_line.split()]]
T = int(entries[0][0])

for i in xrange(1, T+1):
  Z = list(entries[i][0])
  t = len(Z) - 1
  res = 0

  while t >= 0 and Z[t] == '+':
    t -= 1

  if t > 0:
    res += 1

  while t > 0:
    if Z[t] != Z[t-1]:
      res += 1
    t -= 1

  if (Z[0] == '-' and res % 2 == 0) or (Z[0] == '+' and res % 2 == 1):
    res += 1

  print "case #%d: %d" % (i, res)
