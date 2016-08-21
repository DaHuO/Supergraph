for i in range(int(input())):
	N=int(input())
	v=[0]*10
	n=0
	while N != 0 and v.count(0):
		n += N
		for j in str(n):v[int(j)]+=1
	print("Case #" + str(i+1) + ": " + ("INSOMNIA" if n==0 else str(n)))
