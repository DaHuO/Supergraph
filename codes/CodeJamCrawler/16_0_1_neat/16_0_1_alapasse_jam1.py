def last_number(L):
	N = int(L[0])
	res = "INSOMNIA"
	inter = 0
	liste = [0]*10
	if N == 0:
		return res
	else:
		while liste != [1]*10:
			inter += N
			for i in str(inter):
				u = int(i)
				liste[u]=1
			res = inter
		return str(res)



def solution_jam1():
	source = open("D:/Google/QualifJamCode16/A-large.in","r")
	output = open("D:/Google/QualifJamCode16/jamLarge.txt","w")
	liste = source.readline()
	liste = liste.split('\n')
	for i in range(int(liste[0])):
		liste = source.readline()
		liste = liste.split()
		output.write('Case #'+str(i+1)+': '+last_number(liste)+'\n')
	output.close()
	source.close()

solution_jam1()