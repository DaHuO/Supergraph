t = int(input())
for test in range(1,t+1):
	digits = {0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9}
	n = int(input())
	nlist = str(n)
	i = 1
	print('Case #',test,': ',end='',sep='')
	while 1:
		ni = n*i
		nlist = str(ni)

		for j in range(len(nlist)):
			key = (int) (nlist[j])
			if key in digits:
				del digits[key]

		if not digits:
			print(ni)
			break

		i += 1
		if i*n == ni:
			print('INSOMNIA')
			break
		
	



		

	





