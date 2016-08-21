import os

#Stocker str dans liste
def stock(string):
	liste = [""] * len(string)
	for i in range(0, len(string)):
		liste[i] = string[i:i+1]
	return liste


#Inverse l'indice nb et tt les indices avant
def invert(nb, listea):
	c = nb
	d = 0
	listeb = list(listea)
	while c >= 0:
		listeb[d] = listea[c]

		c -= 1
		d += 1

	for index in range(0, nb+1):
		if listeb[index] == "-":
			listeb[index] = "+"
		else:
			listeb[index] = "-"


	return listeb

tour = int(input())

for case in range(1, tour+1):
	
	liste = list(stock(input()))
	liste_t = ["+"] * len(liste)
	counter = 0

	while liste != liste_t:
		nc = -1
		nt = -1
		x = 0
		y = 0

		while x < len(liste):
			if liste[x] == "+":
				nc += 1
				x += 1
			else:
				x = len(liste)

		if nc != -1:
			liste = list(invert(nc, liste))
			counter += 1

		while y < len(liste):
			if liste[y] == "-":
				nt += 1
				y += 1
			else:
				y = len(liste)

		if nt != -1 :
			liste = list(invert(nt, liste))
			counter += 1

	print("Case #" + str(case) + ": " + str(counter))

os.system("pause")
