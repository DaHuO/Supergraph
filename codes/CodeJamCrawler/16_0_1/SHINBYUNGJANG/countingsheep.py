c=int(raw_input())
for i in range(c):
	count=0
	N=raw_input()
	if N =="0":
		print "Case #" + str(i+1) + ": " +"INSOMNIA"
	else:
		y=0
		Number=set()
		while count <10:
			
			count=0
			y=y+1
			M=y*int(N)
			Number=Number.union(set(str(M)))
			
			for j in range(10):
				if str(j) in Number:
					count=count+1

			if count ==10:
				print "Case #" + str(i+1) +": "+ str(M)
			





			
	
			




