IN = "A.in"
OUT = "A.out"

fin = open(IN, 'r')
fout = open(OUT, 'w')

n = int(fin.readline())

for i in range(1,n+1):
	num = fin.readline()
	if num[0] == '0':
		fout.write("Case #" + str(i) + ": INSOMNIA\n")
	else:
		have = set()
		
		for j in range(len(num)):
			if(num[j] == '0'):
				have.update([0])
			elif(num[j] == '1'):
				have.update([1])
			elif(num[j] == '2'):
				have.update([2])
			elif(num[j] == '3'):
				have.update([3])
			elif(num[j] == '4'):
				have.update([4])
			elif(num[j] == '5'):
				have.update([5])
			elif(num[j] == '6'):
				have.update([6])
			elif(num[j] == '7'):
				have.update([7])
			elif(num[j] == '8'):
				have.update([8])
			elif(num[j] == '9'):
				have.update([9])
				
		k = 2
		orig = int(num)
		while len(have) < 10:
			num = str(orig*k)
			k = k + 1
			for j in range(len(num)):
				if(num[j] == '0'):
					have.update([0])
				elif(num[j] == '1'):
					have.update([1])
				elif(num[j] == '2'):
					have.update([2])
				elif(num[j] == '3'):
					have.update([3])
				elif(num[j] == '4'):
					have.update([4])
				elif(num[j] == '5'):
					have.update([5])
				elif(num[j] == '6'):
					have.update([6])
				elif(num[j] == '7'):
					have.update([7])
				elif(num[j] == '8'):
					have.update([8])
				elif(num[j] == '9'):
					have.update([9])
		
		fout.write("Case #" + str(i) + ": " + num + "\n")
	
fin.close()
fout.close()