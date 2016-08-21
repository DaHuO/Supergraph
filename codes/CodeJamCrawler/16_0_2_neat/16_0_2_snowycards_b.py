
def score(word):
	score = 0
	for i in range(0, len(word)):
		if word[i] == '-':
			score += 1
		else:
			break

	for i in reversed(range(0, len(word))):
		if word[i] == '+':
			score += 1
		else:
			break

	if score == len(word) and word[0] == '+':
		score += 1

	return score

def blockAnalysis(word):

	curr = word[len(word) - 1]
	if curr == '-':
		blocks = 1
	else:
		blocks = 0

	for i in reversed(range(0, len(word))):
		if word[i] != curr:
			curr = word[i]
			blocks += 1

	return blocks

if __name__ == '__main__':

	import sys

	cases = int(sys.stdin.readline().split()[0])
	for case in range(1, cases + 1):
		start = sys.stdin.readline().split()[0]

		flips = blockAnalysis(start)


		print "Case #" + str(case) + ": " + str(flips)
				
