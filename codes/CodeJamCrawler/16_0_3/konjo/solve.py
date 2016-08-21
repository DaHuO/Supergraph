T = int(input())
for t in range(1,T+1) :
	print("Case #{}:".format(t))
	s = input()
	ss = s.rstrip().split()
	N = int(ss[0])
	J = int(ss[1])

	candidate = (1 << (N-1)) + 1
	output_cnt = 0
	while output_cnt < J :
		flg = True
		divisor = []
		#base
		for i in range(2, 11) :
			a = 0
			for j in range(N-1, -1, -1) :	
				a *= i
				if candidate & (1 << j) :
					a += 1

			found = False
			for j in range(2,10000) :
				if j >= a :
					break;
				if a % j == 0 :
					found = True
					divisor.append(j)
					break
			
			if not found :
				flg = False

		if flg :
			print(bin(candidate)[2:], " ".join([str(i) for i in divisor]))
			output_cnt += 1
		candidate += 2
