import sys

filename = sys.argv[1]

f = open(filename)
cases = int(f.readline())


for case in range(0, cases):
	S = f.readline().strip()

	# compose all possible words
	
	lastWord = S[0]

	for c in S[1:]:
		if lastWord[0] <= c:
			lastWord = c + lastWord
		else:
			lastWord = lastWord + c

	print('Case #%d: %s' % (case + 1, lastWord))