testcases= int(raw_input())
f = open("codejamop.txt",'w')
for m in range(0,testcases):
	N = int(raw_input())
	tracker=[]
	counter=0
	count=1

	while len(tracker)!=10:
		if N==0:
			temp = "INSOMNIA"
			break
		else:
			temp = count*N
		#print "temp-> ",temp
			counting = list(str(temp))
		#print counting
		#print "Counting-->",counting
			for i in counting:
				if i not in tracker:
					tracker.append(i)
					counter+=1
			
		count+=1
	f.write("Case #%d: %s\n" % (m+1,str(temp)))		
#print counting
#print tracker
f.close()
