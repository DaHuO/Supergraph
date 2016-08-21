import sys
from itertools import islice

if len(sys.argv) != 2:
	print("ERROR: Please specify input")
	exit(1)

"""
 ZRO
   ON
   O W
  R   
  RO  FU
      F 
        SX
    N   S
          G
    N
"""

with open(sys.argv[1]) as f:
	for case, line in islice(enumerate(f), 1, None):
		letter_counts = {letter:line.count(letter) for letter in "ZRONWFUSXG"}
		digit_counts = [0]*10
		digit_counts[6] = letter_counts['X']
		letter_counts['S'] -= letter_counts['X']
		digit_counts[0] = letter_counts['Z']
		letter_counts['R'] -= letter_counts['Z']
		letter_counts['O'] -= letter_counts['Z']
		digit_counts[8] = letter_counts['G']
		digit_counts[4] = letter_counts['U']
		letter_counts['F'] -= letter_counts['U']
		letter_counts['O'] -= letter_counts['U']
		letter_counts['R'] -= letter_counts['U']
		digit_counts[2] = letter_counts['W']
		letter_counts['O'] -= letter_counts['W']
		digit_counts[7] = letter_counts['S']
		letter_counts['N'] -= letter_counts['S']
		digit_counts[5] = letter_counts['F']
		digit_counts[1] = letter_counts['O']
		letter_counts['N'] -= letter_counts['O']
		digit_counts[9] = letter_counts['N']//2
		digit_counts[3] = letter_counts['R']
		print("Case #{}: ".format(case), end="")
		for digit, count in enumerate(digit_counts):
			print(str(digit)*count, end="")
		print("")
