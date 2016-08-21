T = int(input())
for case in range(1,T+1):
	N = int(input())
	if N == 0:
		res = 'INSOMNIA'
	else:
		i = 0
		digits = set()
		while len(digits) < 10:
			i += 1
			res = i*N
			for digit in str(res):
				digits.add(digit)
	print("Case #", case, ": ", res, sep="")