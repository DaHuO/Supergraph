import sys

words = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']

words_by_letter = ['' for _ in range(0, len(words))]
for i in range(0, len(words)):
	words_by_letter[i] = list(0 for _ in range(ord('A'), ord('Z') + 1))
	for j in range(0, len(words[i])):
		words_by_letter[i][ord(words[i][j]) - ord('A')] += 1

lines = sys.stdin.readlines()

test_cases = int(lines[0].strip())

for test_case in range(1, test_cases + 1):

	line = lines[test_case].strip()
	
	available = list(0 for _ in range(ord('A'), ord('Z') + 1))
	for i in range(0, len(line)):
		x = ord(line[i]) - ord('A')
		available[x] += 1
	output = ''
	
	work_items = [('', 0, available)]
	
	answer_found = False
	while(not answer_found and len(work_items) > 0):
		(output, i, available) = work_items.pop()		
		
		if sum(available) == 0:
			answer_found = True
			continue
		
		if i + 1 < len(words_by_letter):
			work_items.append((output, i + 1, available))
		
		next_word = False
		j = 0
		while(not next_word and j < len(words_by_letter[i])):
			if available[j] < words_by_letter[i][j]:
				next_word = True
				continue
			j += 1
			
		if not next_word:
			output += chr(ord('0') + i)
			available = list(available)
			for j in range(0, len(available)):
				available[j] -= words_by_letter[i][j]
			work_items.append((output, i, available))
			
	print 'Case #%d: %s' % (test_case, output)
