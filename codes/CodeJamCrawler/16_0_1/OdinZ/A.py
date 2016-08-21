t = int(input())
for cs in range(t):
	n = int(input())
	print("Case #%d: " % (cs+1), end="")
	if n == 0:
		print("INSOMNIA")
		continue
	digits = [False] * 10
	cnt = 10
	ni = n
	while cnt > 0:
		for sd in str(ni):
			d = int(sd)
			if not digits[d]:
				cnt -= 1
				digits[d] = True
		ni += n
	print(ni - n)