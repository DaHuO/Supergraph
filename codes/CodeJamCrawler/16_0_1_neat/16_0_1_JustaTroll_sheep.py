t = int(input())  # read a line with a single integer

def fufu(n):
	if (n==0):
		return "INSOMNIA"
	l = []
	flag = 0
	for i in range(0,10):
		l.append(0)
	i = 1
	r=1
	while (flag==0):
		m = i * n
		r = m
		#print (m)
		while (m):
			j = int(m%10)
			if (l[j]==0):
				l[j]=1
			m = m//10
		flag = 1
		for k in range(0,10):
			if l[k]==0:
				flag=0
				break
			
				
		i = i+1
	return r



for i in range(1, t+1):
  s = int(input())  # read a list of integers, 2 in this case
  #print (s)
  print ("Case #{}: {} ".format(i, fufu(s)))