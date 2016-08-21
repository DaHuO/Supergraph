def IsPrime( n ):
	if n<=1:
		return [0,0]
	elif n<=3:
		return [1,0]
	elif n%2 == 0:
		return [0,2]
	elif n%3 == 0:
		return [0,3]
	i=5
	while i*i<=n:
		if n%i == 0:
			return [0,i]
		elif n%(i+2)==0:
			return [0,i+2]
		i=i+6
	return [1,0]

def BaseN2Base10( S, Base ):
	i=len(S)-1
	Multiplier = 1
	Result = 0
	while i>=0:
		Result = Result + (int(S[i])*Multiplier)
		Multiplier = Multiplier*Base
		i=i-1
	return Result

Input=open('C-small-attempt0.in','r')
Output=open('output.out','w')

T = int(Input.readline())
if T!=1:
	print "T is out of range"
else:
	Temp = Input.readline().split(' ')
	N = int(Temp[0])
	J = int(Temp[1])
	NumOfJamCoin = 0
	Output.write("Case #1:\n")
	while NumOfJamCoin < J:
		MaxTemp = []
		for i in range(N-2):
			MaxTemp.append('1')
		Max = BaseN2Base10(MaxTemp, 2)
		for i in range(Max+1):
			S = list('1'+format(i, '0'+str(N-2)+'b')+'1')
			IsJamCoin = 0
			Divisors = []
			for j in range(2,11):
				Chk = IsPrime(BaseN2Base10( S,j))
				if(Chk[0]==1):
					IsJamCoin=0
					break
				else:
					Divisors.append(Chk[1])
					IsJamCoin=1
			if IsJamCoin==1:
				NumOfJamCoin = NumOfJamCoin+1
				Output.write("".join(S))
				for j in range(len(Divisors)):
					Output.write(" "+str(Divisors[j]))
				Output.write("\n")
			if NumOfJamCoin == J:
				break
Input.close()
Output.close()
				