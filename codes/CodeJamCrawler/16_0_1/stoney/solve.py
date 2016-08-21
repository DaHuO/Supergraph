INPUT_FILE = "in.txt"

entries = []
with open(INPUT_FILE, 'r') as fin:
  for raw_line in fin.readlines():
    entries += [[int(x) for x in raw_line.split()]]
T = entries[0][0]

MAX_TRIES = 3000

for i in xrange(1, T+1):
  N = int(entries[i][0])
  found = [False] * 10
  tries = 0
  while not all(found) and tries < MAX_TRIES:
    tries += 1
    t = N * tries
    found[t % 10] = True
    while(t > 0):
      found[t % 10] = True
      t = t / 10
#    print tries, N * tries, found
  if tries == MAX_TRIES:
    print "case #%d: INSOMNIA" % i
  else:
    print "case #%d: %d" % (i, N * tries)
