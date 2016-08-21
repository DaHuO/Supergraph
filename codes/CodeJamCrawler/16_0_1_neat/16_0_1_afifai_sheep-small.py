def hitung(x):
	angka = []
	i = 1
	hasil1 = 0
	while set(angka) != {1,2,3,4,5,6,7,8,9,0} :
		hasil = x * i
		if hasil1 == hasil:
			break
		hasil1 = hasil
		y = str(hasil)
		for j in range(len(y)):
			angka.append(eval(y[j]))
		angka = list(set(angka))
		i += 1
	if hasil1==hasil and set(angka) != {1,2,3,4,5,6,7,8,9,0}:
		return "INSOMNIA"
	else:
		return hasil
T = input()
inp = 0
while inp<T:
	inp += 1
	x = input()
	print "Case #"+str(inp)+": "+str(hitung(x))
