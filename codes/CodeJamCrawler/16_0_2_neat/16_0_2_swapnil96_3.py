def pan(array):

	length = len(array)
	dp =0 
	count = 0
	
	if array[0] == '-':

		y = 1
		if length == 1:
			return 1

		while array[y] == '-':
			y += 1
			if y == length:
				return 1

		while array[y] == '+':
			y += 1
			if y == length:
				return 1

		count = 1
		dp = y		
	
	else:
		
		if length == 1:
			return 0

		u = 0
		while array[u] == '+':
			u += 1
			if u == length:
				return 0

		dp = u		

	while dp != length:
		
		j = dp
		k = 0
		l = 0

		while array[j] == '+':
			l += 1
			j += 1
			if j == length:
				break
		
		dp += l
		if dp == length:
			break

		while array[j] == '-':
			k += 1
			j += 1
			if j == length:
				break

		dp += k
		count += 2			

	return count

a = int(raw_input())
que = []

for i in range (0, a):
	v = raw_input()
	que.append(v)

sol = []

for h in range(0, a):
	
	sol.append(pan(que[h]))	

fo = open('foo3.txt', 'w')

for  g in range(0, a):	
	fo.write("Case #%d: %d \n" % (g+1, sol[g]))






