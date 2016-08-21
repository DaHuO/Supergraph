from functools import lru_cache
from itertools import count


errNums = [0, 142857]
decimalDigits = {'0','1','2','3','4','5','6','7','8','9'}

T = int(input())
N = []

for t in range(0,T):
	N.append(int(input()))

for t in range(0,T):
	n = N[t]

	print("case #" + str(t+ 1) +": ", end="")

	if n in errNums:
		print("INSOMNIA")
	else:
		digits= set()

		for t in count(1,1):
			case =n*t
			st = list(str(case))
			digits = digits | set(st)
	
			if (digits == decimalDigits):
				print(str(case))
				break
