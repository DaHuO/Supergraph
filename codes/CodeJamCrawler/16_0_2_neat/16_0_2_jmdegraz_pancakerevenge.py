T = int(input())

for t in range(T):
	S = [k for k in reversed(input())]
	flips = 0

	for i in range(len(S)):
		if S[i] == '-':
			flips += 1
			for j in range(len(S) - i):
				if S[i+j] == '-':
					S[i+j] = '+'
				elif S[i+j] == '+':
					S[i+j] = '-'

	print("Case #%s: %s" % (t + 1, flips))