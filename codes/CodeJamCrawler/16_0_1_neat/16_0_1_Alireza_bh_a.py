T = input()
case = 1
while T>0:
	
	n = input()
	if n==0:
		ans = "INSOMNIA"
	else:
		digits = [0]*10
		i = 1
		num = 0
		while len(filter(lambda x:x==0,digits))>0:
			num = i*n
			t = num
			while t>0:
				digits[t%10]=1
				t/=10
			i+=1
		ans = num
	print "Case #{}: {}".format(case,ans)
	case += 1
	T -= 1
