'''
Google Code Jam 2016
Round 1A
Problem A - The Last Word
'''

import sys

sys.stdout
cases = int(raw_input())

for case in range (0, cases):
	s = []
	for i in raw_input():
		s.extend(i)
		
	alphabet ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	number = []
	y = ""
	for i in range (0, len(alphabet)):
		if s[0] == alphabet[i]:
			number.append(i)
			s.remove(s[0])
			break
	for i in s:
		# first i = start
		# if i > final[0]: insert.(0, i)
		# else append.i
		
		for j in range (0, len(alphabet)):
			if i == alphabet[j]:
				if j >= number[0]:
					number.insert(0, j)
				else:
					number.append(j)
	for i in range (0, len(number)):
		y += alphabet[number[i]]
		
	print ("Case #{}: {}".format(case + 1, y))