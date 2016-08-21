T = int( input().strip() )

for t in range(T) :

	S = input().strip()

	nE = S.count('E')
	nF = S.count('F')
	nG = S.count('G')
	nH = S.count('H')
	nI = S.count('I')
	nN = S.count('N')
	nO = S.count('O')
	nR = S.count('R')
	nS = S.count('S')
	nT = S.count('T')
	nU = S.count('U')
	nV = S.count('V')
	nW = S.count('W')
	nX = S.count('X')
	nZ = S.count('Z')

	N = [0 for i in range(10)];

	#0
	N[0] = nZ
	nZ = 0
	nE -= N[0]
	nR -= N[0]
	nO -= N[0]

	#2
	N[2] = nW
	nT -= N[2]
	nW = 0
	nO -= N[2]

	#4
	N[4] = nU
	nF -= N[4]
	nO -= N[4]
	nU = 0
	nR -= N[4]

	#5
	N[5] = nF
	nF = 0
	nI -= N[5]
	nV -= N[5]
	nE -= N[5]

	#6
	N[6] = nX
	nS -= N[6]
	nI -= N[6]
	nX = 0

	#7
	N[7] = nS
	nS = 0
	nE -= N[7]
	nV -= N[7]
	nN -= N[7]

	#1
	N[1] = nO
	nO = 0
	nN -= N[1]
	nE -= N[1]

	#9
	N[9] = nN // 2
	nN = 0
	nI -= N[9]
	nE -= N[9]

	#8
	N[8] = nG
	nE -= N[8]
	nI -= N[8]
	nG = 0
	nH -= N[8]
	nT -= N[8]

	#3
	N[3] = nT
	nT = 0
	nH -= N[3]
	nR -= N[3]
	nE -= 2*N[3]

	print('Case #', t+1, ': ', sep = '', end = '')
	for i in range(10) :
		for j in range(N[i]) :
			print(i, end='')
	print()

