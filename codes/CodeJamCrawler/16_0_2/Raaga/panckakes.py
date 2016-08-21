filename = "B-large.in.txt"
f = open("outputlarge.txt","w")

with open(filename) as fn:
	content = fn.readlines()

print "Total Cases:" , content[0]

for i in range(1, len(content)):
	stack=list(content[i].rstrip('\n'))
	#print "Length of stack", len(stack)
	#print "Stack Value:", stack
	flip=0
	allDone =1
	while '-' in stack and allDone:
		for j in range(0,len(stack)):
			if(j+1<len(stack)):
				if(stack[j] == stack[j+1]):
					continue
				else:
					#print "In else part"
					k=0
					flip +=1
					while k<=j:
						#print "k",k
						if stack[k]=='+':
							stack[k]='-'
						else:
							stack[k]='+'
						k +=1
			if j+1 == len(stack) and stack[j] =='-':
				flip +=1
				allDone =0
				break


			#print "Stack after change: ", stack	

	#x = str(raw_input("press enter to continue:"))

	print "Case #%d: %s" % (i,str(flip))
	f.write("Case #%d: %s" % (i,str(flip)))
	f.write("\n")
f.close()
