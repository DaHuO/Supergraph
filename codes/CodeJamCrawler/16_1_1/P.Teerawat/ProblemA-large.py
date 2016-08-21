Input=open('A-large.in','r')
Output=open('output-large.out','w')

T = int(Input.readline())
if T < 0 or T > 100:
	Output.write("T is out of range")
else:
	for i in range(T):
		Output.write("Case #"+str(i+1)+": ")
		Temp = Input.readline().replace('\n','')
		S = list(Temp)
		Answer = []
		Answer.append(S[0])
		for j in range(1,len(S)):
			if S[j] >= Answer[0]:
				Answer.insert( 0, S[j])
			else:
				Answer.append(S[j])
		Output.write("".join(Answer))
		Output.write("\n")
Input.close()
Output.close()
