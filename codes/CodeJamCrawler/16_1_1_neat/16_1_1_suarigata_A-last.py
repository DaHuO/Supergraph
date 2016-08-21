T = int(raw_input())
for t in range(T):
	S=raw_input()
	
	res=[]
	maior=-1
	for s in S:
		if ord(s)>=maior:
			maior=ord(s)
			res.insert(0,s)
		else:
			res.append(s)

	print("Case #" + str(t+1) + ": " + ''.join(res))
