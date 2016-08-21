def CheckDigits(N):
	check = [False]*10
	N_str = str(N)
	for ch in N_str:
		if ((ord(ch) >= 48) and (ord(ch) <= 57)):
			check[int(ch)] = True
	return check

def CheckDigitsList(L,N):
	cdn = CheckDigits(N)
	L = ORarray(cdn,L)
	return L

def ProcessN(N):
	if N == 0:
		return 'INSOMNIA'
	L = [False] * 10
	i = 0;
	while(not(all(L))):
		i = i + 1
		nN = i * N
		L = CheckDigitsList(L,nN)
 	return str(nN)

def ORarray(a,b):
	out = [False]*10
	for i in range(len(a)):
		out[i] = a[i] or b[i]
	return out

f= open('A-large.in','r')
# Read number of trials (T)
T = f.readline()
for t in range(int(T)):
	N = f.readline()
	result = ProcessN(int(N))
	print 'Case #' + str(t+1) +': '+ result
