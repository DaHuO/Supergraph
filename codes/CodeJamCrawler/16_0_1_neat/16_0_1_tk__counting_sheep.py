import sys

T = int(sys.stdin.readline())

for case_num in range(1,T+1):
	N = int(sys.stdin.readline())
	if N == 0:
		print("Case #{0}: INSOMNIA").format(case_num)
	else:
		i = 0
		seen = set()
		while len(seen) < 10:
			i += 1
			# add all the characters from i*N to the seen set
			seen.update(list(str(i*N)))
		print("Case #{0}: {1}").format(case_num, i*N)