import math
Input=open('D-large.in','r')
Output=open('output-large.out','w')

T = int(Input.readline())
if T < 0 or T > 100:
	Output.write("T is out of range")
else:
	for i in range(T):
		Output.write("Case #"+str(i+1)+":")
		PstList=[]
		Temp = Input.readline().split(' ')
		K = int(Temp[0])
		C = int(Temp[1])
		S = int(Temp[2])
		MinCleanNeed = int(math.ceil(float(K)/float(C)))
		if math.ceil(S<MinCleanNeed):
			Output.write(" IMPOSSIBLE\n")
		else:
			Last = 0
			for j in range(1,MinCleanNeed+1):
				Position = 1;
				for p in range(Last+1,Last+C+1):
					if p<K:
						Position = ((Position-1)*K)+p
					else:
						Position = ((Position-1)*K)+K
				Last = Last+C
				Output.write(" "+str(Position))
			Output.write("\n")
Input.close()
Output.close()