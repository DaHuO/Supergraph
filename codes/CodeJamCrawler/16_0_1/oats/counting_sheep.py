#
#	Arshan Alam
#
#	Google Code Jam 2016
#
#	Problem A - Counting Sheep
#

for test in range(1, int(input())+1):
	n = N = int(input())
	
	if N is 0:
		print("Case #" + str(test) + ": INSOMNIA")
		continue
	
	counter = 1
	remaining = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	
	prev_len = len(remaining)
	while prev_len > 0:
		n = counter * N
		for c in str(n):
			digit = int(c)
			if digit in remaining:
				remaining.remove(digit)
		prev_len = len(remaining)
		counter += 1
	print("Case #" + str(test) + ": " + str(n))
