import sys

ncases = int(sys.stdin.readline())
for _c in range(ncases):
	n = int(sys.stdin.readline())
	if n == 0: print("Case #%d: INSOMNIA" % (_c+1))
	else:
		seenD = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		seenC = 0
		i = 1
		while True:
			s = str(n*i)
			for c in s:
				idx = int(c)
				if seenD[idx] == 0:
					seenD[idx] = 1
					seenC += 1
			if seenC == 10:
				print("Case #%d: %s" % (_c+1, s))
				break
			i += 1
