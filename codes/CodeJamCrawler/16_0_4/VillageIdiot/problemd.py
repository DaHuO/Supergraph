import sys


def doTest(args):
  K,C,S = map(int, args.split())
  return " ".join([str(i+1) for i in range(S)])
  
inlines = open(sys.argv[1]).readlines()
numcases = int(inlines[0])
idx = 1

for case in range(numcases):
    print "Case #%d: %s" % (case + 1, doTest(inlines[idx]) )
    idx += 1
