

T = int(input())



for case in range(T):
	N = int(input())
	digits = []
	counter = 1
	if N == 0:
		s = "INSOMNIA"
	else:
		while len(digits) < 10:
			s = str(int(N)*counter)
			for i in s:
				if i not in digits:
					digits.append(i)
			counter += 1
	print("Case #{}: {}".format(case+1, s))
	
	
		



