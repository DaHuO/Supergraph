#!/usr/bin/python
# -*-coding:Utf-8 -*

f = open("input1",'r')
lignes  = f.readlines()
f.close()

line1 = lignes[0]

del lignes[0]

numbers = []
insomnia = 0
retour = 0

j = 1
for l in lignes:
	insomnia = 0
	N = int(l)

	is_finished = 0

	if (N == 0):
		insomnia = 1

	i = 1
	while (is_finished == 0 and insomnia == 0):
		retour = N*i
		string = str (retour)
		for s in string:
			if (s not in numbers):
				numbers.append(int(s))
				
		is_finished = 1
		for t in xrange(0,10):
			if (not t in numbers):
				is_finished = 0
				break

		i = i+1
		


	#Writing in the file
	f = open("output1",'a')
	if (insomnia == 1):
		f.write("Case #{}: INSOMNIA\n" . format(j))
	else:
		f.write("Case #{0}: {1}\n" . format(j, retour))
	f.close()

	j=j+1
	numbers[:] = []
