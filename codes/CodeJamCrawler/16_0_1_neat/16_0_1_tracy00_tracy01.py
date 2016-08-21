#test cases
t = raw_input()
t=int(t)

case = 0

for i in range(0,t):
	case+=1
	#input number
	n = raw_input()
	n=int(n)
	if(n==0):
		print("Case #"+str(case)+": ""INSOMNIA")

	else:
		dorm = [0 for i in range(10)]
		reached = 0
		klpd = 0
		count = 1
		
		while(klpd==0):
			tmp = n*count
			while(tmp!=0):
				if(dorm[tmp%10]==0):
					dorm[tmp%10]=1
					reached=reached+1
					if(reached==10):
						klpd=1
						break
				tmp=tmp/10
			count=1+count
		
		print("Case #"+str(case)+": "+str(n*(count-1)))

