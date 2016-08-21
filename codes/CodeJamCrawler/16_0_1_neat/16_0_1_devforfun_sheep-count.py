t = int(raw_input())  

for i in xrange(1, t + 1):
	n = str(raw_input())  
	digits=["0","1","2","3","4","5","6","7","8","9"]
	found=[]
	sleeped=False
	result=""

	if n=="0":
		result="INSOMNIA" 
	
	else:
		
		j=1

		while sleeped==False: 
			number=str(j*int(n))
			result=number

			#recorro la lista 
			for digit in digits:

				#encuentro el char  
				if digit in  number:
					#lo quito de lista y del numero
					found.extend(digit)
					number=number.replace(digit,"")

				#si encontre todos los valores me dormi
				if len(found)==10:
					sleeped=True 

				if len(number)==0:
					break

			digits=set(digits)-set(found)
			j=j+1

			
	print "Case #{}: {}".format(i, result)
