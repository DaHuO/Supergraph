import math

read_file=open(r'A-large.in','r')
input_file=read_file.readlines()
print(input_file)
cases=int(input_file[0])

output=open(r'output6','w')


for case in range(cases):
	#case start from 0
	#print("case:",case+1)
	S=input_file[case+1]
	
	L=[]
	largest= 0
	large = 0


	for ch in S:
		if ord(ch) > largest:
			largest=ord(ch)
			large = ch
	print("large:", large)
	L.insert(0,S[0])
	first=S[0]
	last=S[0]
	print("init L:",L)
	
	for x in range(1,len(S)-1):
		
		if S[x] is not large:
			print(S[x], first)
			if ord(S[x]) >= ord(first):
				L.insert(0,S[x])
				print(L)
				first=S[x]
			elif ord(S[x]) :
				L.append(S[x])
			
		else:
			print ("first:",S[x])
			L.insert(0, S[x])
			first = S[x]
			print(L)
		
	print(L)

	result = ''.join(L)

	c=case+1
	output.write("Case #{}: {}\n".format(c,result))






