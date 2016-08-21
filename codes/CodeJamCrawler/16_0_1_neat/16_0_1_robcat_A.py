import sys
T = int(next(sys.stdin))
for t, line in enumerate(sys.stdin):
	S = N = int(line.strip())
	if N==0:
		S = 'INSOMNIA'
	else:
		digits = set(str(N))
		while len(digits)<10:
			S += N
			digits.update(str(S))
	print("Case #%s:" % (t+1), S)
