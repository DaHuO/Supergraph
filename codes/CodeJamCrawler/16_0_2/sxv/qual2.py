import sys
infile = sys.argv[1]

data = open(infile)
stacks = int(data.readline())

for n in range(stacks):
  flips = 0
  last = '+'
  stack = data.readline().strip()[::-1]
  for p in stack:
    if p != last:
      flips += 1
      last = p
  print "Case #%s: %s" % (n+1, flips)