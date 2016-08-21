from math import sqrt

T = int(input())
for t in range(T):
	if (t==0):
		print("Case #" + str(t+1) + ": ")
	else:
		print("\nCase #" + str(t+1) + ": ")

	N, J = list(map(int,input().split()))
	# # On génère tous les nombres de taille J
	# l = [bin(x)[2:].rjust(N, '0') for x in range(2**N)]
	# # On enlève la première moitié qui commence par 0
	# l = l[int(len(l)/2):]
	# # l = ['100011','111111','111001']
	# # print(l)
	Jam = []
	# On garde le nombre de JamCode trouves
	trouves = 0
	for x in range(2 << N-2):
		i = '1' + str(bin(x)[2:]).zfill(N-2) + '1'
		# On garde les nombres qui commencent et finissent par 1
		# print(i)
		# On va garder un diviseur pour chaque base dans la liste lbis
		lbis = []
		for j in range(2,11):
			C = int(i,j)
			if (C>1):
				for k in range(2,int(sqrt(C))):
					if (k>10000):
						break
					if (C % k) == 0:
						if (k!= 1 and k!= C):
							lbis.append(k)
							break
				else:
					break
			else:
				# Une erreur potentielle
				# Peut etre avec le 0 et 1
				# Qui ne sont pas premiers
				break
			if len(lbis)==9:
				print(i,end="")
				for div in lbis:
					print(" " + str(div),end="")
				print("")
				trouves += 1
		if (trouves >= J):
			break
# # print(trouves)
# # print(Jam)
# for a,b in Jam:
# 	# print("\n" + "{0:b}".format(int(a,10)), end="")
# 	print("\n" + a, end="")
# 	for c in b:
# 		print(" " + str(c),end="")





