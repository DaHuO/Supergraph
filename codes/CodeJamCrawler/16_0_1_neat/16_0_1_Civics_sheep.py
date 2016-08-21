T = input()
for i in range(1,T+1):
	N = input()
	arr = [False,False,False,False,False,False,False,False,False,False]

	if N==0:
		print "Case #" + str(i) + ": INSOMNIA"
	else:
		count = 0
		incr = 1
		ans = N
		while count != 10:
			n = N * incr
			ans = n
			incr += 1
			while n != 0:
				x = n%10
				n /= 10
				#print "x=" +str(x) + "  n="+str(n) + "  count=" + str(count)
				if not arr[x]:
					count += 1
					arr[x] = True 

		print "Case #" + str(i) + ": " + str(ans)


