def maxLetter(letters, start, end):
	maxLetterIndex = start
	for index in range(start + 1, end + 1):
		if letters[index] >= letters[maxLetterIndex]:
			maxLetterIndex = index
	return maxLetterIndex
def answer(caseNum, lastWord):
	print("Case #" + str(caseNum) + ": " + lastWord)
def invert(s, inversions):
	inversions.sort(reverse = True)
	s1 = ''
	for inversion in inversions:
		s1 += s[inversion]
	s2 = ''
	for index in range(len(s)):
		if index not in inversions:
			s2 += s[index]
	return s1 + s2 

cases = int(input())
for case in range(1, cases + 1):
	s = input()
	inversions = []
	start = 0
	end = len(s) - 1
	while end > 0:
		switch = maxLetter(s, start, end)
		end = switch - 1
		inversions.append(switch)
	lastWord = invert(s, inversions)
	answer(case, lastWord)