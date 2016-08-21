import sys
T = int(next(sys.stdin))
for t, line in enumerate(sys.stdin):
	pncs = [pnc=='+' for pnc in line.strip()]
	flips = [i!=j for i, j in zip(pncs[1:]+[True], pncs)]
	print("Case #%i:" % (t+1), flips.count(True))
