def CheckInList( List , Number ):
	for i in range(len(List)):
		if Number==List[i]:
			return 1
	return 0
	
def IsContainAll( List ):
	if len(List)==10:
		return 1
	else:
		return 0

Input=open('A-large.in','r')
Output=open('output-Large.out','w')

T = int(Input.readline())
if T < 0 or T > 100:
	print "T is out of range"
else:
	for i in range(T):
		SeenList=[]
		N = int(Input.readline())
		if N==0:
			Output.write("Case #"+str(i+1)+": INSOMNIA\n")
		else:
			Multiplier = 1
			while True:
				TempN = list(str(N*Multiplier))
				for j in range(len(TempN)):
					if CheckInList(SeenList,TempN[j])==0:
						SeenList.append(TempN[j])
				if IsContainAll(SeenList)==1:
					Output.write("Case #"+str(i+1)+": "+str(N*Multiplier)+"\n")
					break
				else:
					Multiplier = Multiplier+1
	Input.close()
	Output.close()
