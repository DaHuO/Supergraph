#!/usr/bin/python
# -*-coding:Utf-8 -*

def shift (string):
	retour = ""
	for s in string:
		if s == "-":
			retour = retour + "+"
		else:
			retour = retour + "-"

	return retour

def flip (string, i):
	retour = ""
	ind = i-1
	while (ind >= 0):
		retour = retour + string[ind]
		ind = ind - 1

	retour = shift(retour) + string[i:]

	return retour

def countF(string):
	l = string[0]
	string = string[1:]
	i = 1
	for c in string:
		if (c == l):
			i = i + 1
		else:
			break

	return i

def init(string):
	retour = ""
	for i in string:
		retour = retour + "+"

	return retour


f = open("input2",'r')
lignes  = f.readlines()
f.close()

#string = lignes[4].rstrip()
#print ("String : {0}, Shift : {1}, Flip : {2}" . format(string, shift(string), flip(string, 3)))

line1 = lignes[0]

del lignes[0]



j = 1
for l in lignes:
	line = l.rstrip()	
	objectif = init(line)
	print (line)

	optimal = 0
	while (line != objectif):
		count = countF(line)
		#print(count)
		line = flip(line, count)
		print("{0} {1}" . format(line,objectif))
		optimal = optimal + 1



	#Writing in the file
	f = open("output2",'a')
	f.write("Case #{0}: {1}\n" . format(j, optimal))
	f.close()

	j=j+1