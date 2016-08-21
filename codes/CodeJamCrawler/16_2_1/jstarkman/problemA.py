import sys
from collections import deque
line_number = 0

for line in sys.stdin:
	if line_number:
		# code
		letters = [0 for _ in range(26)]
		num = [0 for _ in range(10)]
		for l in line[:-1]:
			letters[ord(l) - ord("A")] += 1
		for z in range(letters[25]): # how many Z for zero
			num[0] += 1
			for p in [26, 5, 18, 15]:
				letters[p - 1] -= 1
		for w in range(letters[22]):
			num[2] += 1
			for p in [20, 23, 15]:
				letters[p - 1] -= 1
		for x in range(letters[23]):
			num[6] += 1
			for p in [19, 9, 24]:
				letters[p - 1] -= 1
		for g in range(letters[6]):
			num[8] += 1
			for p in [5, 9, 7, 8, 20]:
				letters[p - 1] -= 1
		for u in range(letters[20]):
			num[4] += 1
			for p in [6, 15, 21, 18]:
				letters[p - 1] -= 1
		for s in range(letters[18]):
			num[7] += 1
			for p in [19, 5, 22, 5, 14]:
				letters[p - 1] -= 1			
		for v in range(letters[21]):
			num[5] += 1
			for p in [6, 9, 22, 5]:
				letters[p - 1] -= 1
		for t in range(letters[19]):
			num[3] += 1
			for p in [20, 8, 18, 5, 5]:
				letters[p - 1] -= 1
		for o in range(letters[14]):
			num[1] += 1
			for p in [15, 14, 5]:
				letters[p - 1] -= 1
		for e in range(letters[4]):
			num[9] += 1
		x = ""
		for i, n in enumerate(num):
			x = x + str(i)*n
		print("Case #%d: %s" % (line_number, x))
	line_number += 1
