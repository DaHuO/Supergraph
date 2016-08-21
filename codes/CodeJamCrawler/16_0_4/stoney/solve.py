INPUT_FILE = "in.txt"

entries = []
with open(INPUT_FILE, 'r') as fin:
  for raw_line in fin.readlines():
    entries += [[x for x in raw_line.split()]]
T = int(entries[0][0])

for i in xrange(1, T+1):
  K = int(entries[i][0])
  C = int(entries[i][1])
  S = int(entries[i][2])

  R = ""
  p = pow(K, C-1)
  for t in xrange(K):
    R += " %d" % (p * t + 1)
  print "case #%d:%s" % (i, R)
