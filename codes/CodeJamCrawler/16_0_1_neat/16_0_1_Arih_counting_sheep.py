list_tosee= [0,1,2,3,4,5,6,7,8,9]
list_saw=[]
case, N,start = 0,0,1
t = int(raw_input()) 
if (t<=100): 
	for i in xrange(1, t + 1):
		case = i
		n = int(raw_input()) 
		N=n
		stop = 0
		while n <= 1000000 and n!=0:
			start+=1
			n = str(n)
			for x in range(len(n)):
				if int(n[x]) in list_tosee and int(n[x]) not in list_saw:
					list_saw.append(int(n[x]))
				if len(list_saw)==len(list_tosee):
					stop = 1
					break
			if stop:
				break
			n = N*start
		list_saw=[]
		start = 1
		n = int(n)
		if n>1000000 or n==0:
			n = 'INSOMNIA'
		print "Case #{}: {}".format(case,n)