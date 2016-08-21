import sys

alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def solve(n, a):
	total = 0
	for i in range (0, len(a)):
		total = total + a[i]

	if total<=0:
		return 0

	if total == 2:
		for i in range(0, len(a)):
			if a[i] > 0:
				print(alpha[i], end="")
		print()
		return 2

	m = 0
	for i in range(0, len(a)):
		if m < a[i]:
			m = a[i]

	half = (total-1)/2
	if m > half:
		twice = 1
	else:
		twice = 0

	for i in range(0, len(a)):
		if m == a[i]:
			print(alpha[i], end = "")
			a[i] = a[i] - 1
			if twice==0:
				break
			else:
				twice = 0
	print(" ",sep="", end="")
	solve(n, a)
	
t = int(input().strip())
for i in range(1, t+1):
	n = int(input())
	a = [int(a_temp) for a_temp in input().strip().split(' ')]
	print("Case #",i,": ",sep="", end="")
	solve(n, a)
