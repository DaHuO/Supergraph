t = int(raw_input())  

for i in xrange(1, t + 1):
	stack = list(raw_input())  
	movements=0
	next=0	
	size=len(stack)

	#recorro la lista 
	for j, needle in enumerate(stack):

		if size>j+1: 
			# si hay un cambio es un movimiento que hay que hacer 	
			if (stack[j]!=stack[j+1]):
				movements=movements+1
		else:
			# si el ultimo elemento es down hay que voltear toda la pila
			if stack[j]=="-":
				movements=movements+1					

	print "Case #{}: {}".format(i, movements)

