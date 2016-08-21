

t=int(raw_input())


for i in range(t):
	check = [0,1,2,3,4,5,6,7,8,9]
	a=int(raw_input())
	mul = 0
	if a == 0:
		print "Case #" + str(i+1)+": "+ "INSOMNIA"
	else:	
		while True:
			mul=mul+1
			StringA = str(mul*a)
			listA = list(StringA)
			
			for j in listA:
				if int(j) in check:
					check.remove(int(j))
				if len(check)==0:
					print ("Case #"+ str(i+1) +": "+ str(mul*a)) 						
					break
			if len(check)==0:						
					break
