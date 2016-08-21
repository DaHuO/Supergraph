def flips(panstr):
	#print("p",panstr)
	flip = 0;
	#print(1)
	newstr = ""
	for i in reversed(panstr):
		newstr = newstr + i
		#print(i)
	#print("n",newstr)
	i = 0;
	j = len(newstr)+1;
	k = "-"
	while(not newstr.find(k,i) == -1):
		i = newstr.find(k,i)
		j = newstr.find(k,i)
		#print("f",i,j)
		if ( k == "+" ):
			k = "-"
		else:
			k = "+"
		flip = flip + 1
		i = j
	return flip
t = int(input())
for i in range(t):
	panstr = input()
	#print(panstr)
	print("Case #"+str(i+1)+":",str(flips(panstr)))
	
	