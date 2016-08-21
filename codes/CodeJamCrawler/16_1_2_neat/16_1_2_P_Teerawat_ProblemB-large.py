Input=open('B-large.in','r')
Output=open('output-large.out','w')

T = int(Input.readline())
if T < 0 or T > 100:
	Output.write("T is out of range")
else:
	for i in range(T):
		Output.write("Case #"+str(i+1)+":")
		N = int(Input.readline())
		SoldierDict = {}
		MissingList = []
		for j in range(2*N-1):
			Temp = Input.readline().replace('\n','')
			List = Temp.split(' ')
			for k in range(len(List)):
				if SoldierDict.has_key(List[k]):
					SoldierDict[List[k]] = SoldierDict[List[k]]+1
				else:
					SoldierDict[List[k]] = 1
		for key, value in SoldierDict.iteritems():
			if SoldierDict[key]%2 != 0:
				MissingList.append(int(key))
		MissingList.sort()
		for j in range(len(MissingList)):
			Output.write(" "+str(MissingList[j]))
		Output.write("\n")
Input.close()
Output.close()
