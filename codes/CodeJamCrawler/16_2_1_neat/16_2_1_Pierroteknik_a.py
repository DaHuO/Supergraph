import string

T = int(input())
for t in range(T):
	print("Case #" + str(t+1) + ": ",end="")
	# Dico des char reconnus
	letters = list(string.ascii_uppercase)
	dico = {}
	for i in letters:
		dico[i]=0
	# On représente les numéros qu'on a :
	numb = [0,0,0,0,0,0,0,0,0,0]
	S = input()
	for i in S:
		dico[i] += 1
	## Maintenant on retrouve le nombre de chaque chiffre
	nZ = dico["Z"]
	numb[0]=nZ
	dico["E"] -= nZ
	dico["R"] -= nZ
	dico["O"] -= nZ

	dico["Z"] -= nZ


	nW = dico["W"]
	numb[2]=nW
	dico["T"] -= nW
	dico["O"] -= nW
	dico["W"] -= nW

	nX = dico["X"]
	numb[6]=nX
	dico["I"] -= nX
	dico["S"] -= nX
	dico["X"] -= nX

	nU = dico["U"]
	numb[4]=nU
	dico["F"] -= nU
	dico["O"] -= nU
	dico["U"] -= nU
	dico["R"] -= nU

	nF = dico["F"]
	numb[5]=nF
	dico["V"] -= nF
	dico["I"] -= nF
	dico["F"] -= nF
	dico["E"] -= nF

	nV = dico["V"]
	numb[7]=nV
	dico["S"] -= nV
	dico["E"] -= nV
	dico["V"] -= nV
	dico["E"] -= nV
	dico["N"] -= nV

	nG = dico["G"]
	numb[8]=nG
	dico["I"] -= nG
	dico["T"] -= nG
	dico["E"] -= nG
	dico["G"] -= nG
	dico["H"] -= nG
	
	nI = dico["I"]
	numb[9]=nI
	dico["N"] -= nI
	dico["I"] -= nI
	dico["N"] -= nI
	dico["E"] -= nI

	nT = dico["T"]
	numb[3]=nT
	dico["T"] -= nT
	dico["H"] -= nT
	dico["R"] -= nT
	dico["E"] -= nT
	dico["E"] -= nT
	
	numb[1]=dico["N"]

	for i in range(len(numb)):
		for j in range(numb[i]):
			print(i,end="")
	print("")