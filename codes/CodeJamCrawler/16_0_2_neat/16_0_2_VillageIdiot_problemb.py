import sys 

def numFlips(s):
  totalFlips = 0
  idx = len(s) - 1
  while idx >= 0:
    if (s[idx] == '-' and totalFlips % 2 == 0) or (s[idx] == '+' and totalFlips % 2 == 1):
      totalFlips += 1 
    idx -= 1
  return totalFlips 
inlines = open(sys.argv[1]).readlines()
numcases = int(inlines[0])
idx = 1

for case in range(numcases):
    print "Case #%d: %d" % (case + 1, numFlips(inlines[idx])) 
    idx += 1


