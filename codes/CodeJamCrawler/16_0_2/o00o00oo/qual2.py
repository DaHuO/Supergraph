# google code jam shit
# author lee barnett
#
# i hate coding

from string import maketrans

fin = open("input.txt","r")
fout = open("output.txt","w")

non = fin.readline()

k = 0

mapping = maketrans("+-", "-+")

for line in fin.readlines():
	k = k+1
	flipcount = 0
	#newl = line[::-1]
	newl = line.strip()

	while "-" in newl:
		while newl[-1] == '+':	
			newl = newl[:-1]
		if newl[0] == '-': 
			flipcount = flipcount + 1
			newl = newl.translate(mapping)[::-1]
		elif newl[0] == '+':
			index = newl.find("-") - 1
			newl = newl[0:index].translate(mapping) + newl[index+1:]
			flipcount = flipcount + 1

	fout.write("Case #{0}: {1}\n".format(k,flipcount))

fin.close()
fout.close()
