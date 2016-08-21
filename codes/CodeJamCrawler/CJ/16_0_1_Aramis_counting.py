from sys import stdin
for _t in xrange(1,int(stdin.next())+1):
	N = int(stdin.next())
	if N == 0:
		out = "INSOMNIA"
	else:
		out = 0
		digits = []
		temp_N = N
		while temp_N > 0:
			digit = temp_N % 10
			if digit not in digits:
				out += 1
				digits.append(digit)
			temp_N /= 10
		# print digits,N,out
		i = 2
		while len(digits) < 10:
			out = next_N = N*i
			while next_N > 0:
				digit = next_N % 10
				if digit not in digits:
					digits.append(digit)
				next_N /= 10
			i += 1
			next_N *= i
	print "Case #"+str(_t)+":",out