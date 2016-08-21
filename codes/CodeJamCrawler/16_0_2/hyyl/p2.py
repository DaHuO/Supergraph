def flip(currstring):
	for i in range(len(currstring)):
		if currstring[i]=='+':
			currstring[i]='-'
		else:
			currstring[i]='+'





T=int(input())

for i in range(T):
	currstring=list(input())
	currstring.reverse()
	flips=0


	#find the smallest down pancake
	#remove pancakes before that
	#flip all the pancakes 
	#repeat

	while True:
		try:
			newtop=currstring.index('-')
		except ValueError:
			break
		
		currstring=currstring[newtop:]
		flips+=1
		flip(currstring)

	print("Case #%d: %d" %(i+1,flips) )