t = int(input())
for i in range(t):
	k = ""
	s = input()
	for j in s:
		if not len(k) > 0:
			k = k.__add__(j)
		else:
			if( ord(j) >= ord(k[0]) ):
				k = j.__add__(k)
			else:
				k = k.__add__(j)
			#print(k,ord(i),ord(k[0])
	print("Case #"+str(i+1)+": "+str(k) , sep="")