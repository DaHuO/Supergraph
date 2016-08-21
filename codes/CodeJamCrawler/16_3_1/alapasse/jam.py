def maxim(liste):
	res = 0
	ind = 0
	for i in range(len(liste)):
		if liste[i] > res:
			res = liste[i]
			ind = i
	return (res,ind)

def max2(liste,max1):
	res = 0
	ind = 0
	for i in range(len(liste)):
		if liste[i] > res and i != max1:
			res = liste[i]
			ind = i
	return (res,ind)

def mot(liste):
	res = ''
	for c in liste:
		res = res +' ' + c
	return res

def function(a,liste):
	(maxi,ind) = maxim(liste)
	(maxi2,ind2) = max2(liste,ind)
	out = []
	for i in range(maxi2,maxi):
		out = out + [chr(ind+65)]
	for i in range(len(liste)):
		if i != ind:
			if i!= ind2:
				out = out+[chr(i+65)]*liste[i]
	out = out + [chr(ind+65)+chr(ind2+65)]*maxi2
	return mot(out)


def solution_jam():
	source = open("D:/Google/QualifJamCode16/A-large.in","r")
	output = open("D:/Google/QualifJamCode16/solution.txt","w")
	liste = source.readline()
	liste = liste.split('\n')
	for i in range(int(liste[0])):
		liste1 = source.readline()
		a = int(liste1)
		liste2  = source.readline()
		liste = liste2.split(' ')
		print(liste)
		liste = [int(b) for b in liste]
		print(liste)
		output.write('Case #'+str(i+1)+': '+function(a,liste)+'\n')
	output.close()
	source.close()

solution_jam()