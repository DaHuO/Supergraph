for _ in range(input()):
	no = int(raw_input())
	arr = ["1","2","3","4","5","6","7","8","9","0"]
	if(no == 0):
		print "Case #"+str(_+1)+": INSOMNIA"
		continue
	k = 0
	while(len(arr)!=0):
		k +=  no
		for i in str(k):
			if((i) in arr):
				arr.remove(i)
		
	print "Case #"+str(_+1)+": "+str(k)


	
		



		
