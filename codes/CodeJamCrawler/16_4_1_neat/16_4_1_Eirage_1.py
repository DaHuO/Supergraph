def sp(a,b,c):
	if (a+b+c == 2):
		if a == 0:
			return ('PS')
		elif b == 0:
			return('RS')
		else:
			return('PR')
	else:
		m = max(a,b,c)
		a1 = m // 2
		b1,c1 = a1, a1
		if a1 * 2 != a:
			a1 = a - a1
		elif b1 * 2 != b:
			b1 = b - b1
		else:
			c1 = c - c1
		x = sp(a1,b1,c1)
		y = sp(a-a1,b-b1,c-c1)
		if x < y:
			return x + y
		else:
			return y + x





T = int(raw_input())  
#n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case

for K in range (T):
	N,r,p,s = [int(s) for s in raw_input().split(" ")]
	n = 2 ** N
	n = n // 3 
	if (0<= r - n <= 1) and (0<= p - n <= 1) and (0<= s - n <= 1):
		ret = sp(r,p,s)
		print "Case #{}: {}".format(K+1, ret)


	else:
		print "Case #{}: {}".format(K+1, 'IMPOSSIBLE')
		