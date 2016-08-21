from math import sqrt

T = int(input())

for t in range(T):
	print("Case #{}:".format(t+1))
	N, J = list(map(int,input().split()))

	#listJamCoinToTest = [('1'+ str(bin(e)[2:]).zfill(N-2) + '1') for e in range(2 << N-2)]

	#listJamCoin = []
	nbJamCoin = 0

	for e in range(2 << N-2):
		jamCointToTest = '1'+ str(bin(e)[2:]).zfill(N-2) + '1'
		l = []
		l.append(jamCointToTest)
		isJamCoin = True
		for base in range(2,10+1):
			A = int(jamCointToTest,base)
			divisorFound = False
			for i in range(2,min(int(sqrt(A)),100000)):
				if A % i == 0:
					l.append(str(i))
					divisorFound = True
					break
			if not divisorFound:
				isJamCoin = False
				break
		if isJamCoin:
			#listJamCoin.append(l)
			print(" ".join(l))
			nbJamCoin += 1
			if nbJamCoin == J:
				exit()
