def Reverse(stack,ref):
	for i in range(ref):
		if(stack[i]== "+"):
			stack[i] = "-"
		else:
			stack[i] = "+"

# Main
t = int(input())

for i in range(t):
	stack = list(input());
#	print("bgn",stack)
	ref = len(stack)
	counter = 0
	
	while(ref > 0):
	#check if last val is -
		if(stack[ref-1] == "-"):
			plusref = 0
	# count nb of + at bgn of stack
			while(stack[plusref] == "+"):
				plusref = plusref + 1
	# if first values are + reverse stack from bgn to plus ref
			if (plusref > 0):
				Reverse(stack,plusref)
				counter = counter + 1
#				print(stack)	
	# reverse stack from bgn to ref 
			Reverse(stack,ref)
			counter = counter + 1
#			print("end",stack)

		ref = ref - 1
		
	print("Case #{}: {}".format(i+1, counter))