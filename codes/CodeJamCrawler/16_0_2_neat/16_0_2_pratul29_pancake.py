tc = int(input())
for i in range(1,tc+1):
	ans1 = 'Case #'+str(i)+': '
	a = input()
	len_inp = len(a)
	step = 0
	number_pluses = a.count('+')
	while len_inp != number_pluses:
		step +=1
		if number_pluses == 0:
			break
		if a[0] == '+':
			p = a.index('-')
			a = '-' * p + a[p:];
			number_pluses -= p;
		else:
			p = a.index('+')
			a = '+' * p + a[p:];
			number_pluses += p;
	ans1 = ans1 + str(step)
	print(ans1)
